from llm.user import call_llm
from prompt_engine.builder import build_prompt_base
from prompt_engine.builder import build_explication
from prompt_engine.builder import build_examples
from prompt_engine.builder import build_questions
from prompt_engine.builder import build_visual_resumo
from prompt_engine.mock import Mock
import json
from datetime import datetime, timezone
import os
from flask import Flask, render_template, request
from typing import Any

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    topic = request.form["topic"]
    prompt_option = request.form["prompt_option"]
    try:
        age = int(request.form["age"])
    except (ValueError, KeyError):
        return "Idade Inválida"
    level = request.form["level"]
    howLearning = request.form["howLearning"]

    outputs = generate_main(name, age, level, howLearning, topic, prompt_option)

    return render_template("result.html", outputs=outputs)


def load_data(path: str, default: any) -> Any:
    if not os.path.exists(path):
        return default
    try:
        with open(path, 'r', encoding = 'utf-8') as file:
            return json.load(file)
    except json.JSONDecodeError:
            return default
            
def save_data(path: str, data: any) -> bool:
    try:
        with open(path, 'w', encoding= 'utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
            return True
    except OSError:
        return False
    
def generate_new_response(name: str, age: int,  level: str, howLearning: str, topic: str, time_now: str, version: str) -> dict[str, Any]:
    prompt_base = build_prompt_base(name, age, level, howLearning)

    #explicação
    result_explication = call_llm(build_explication(topic, prompt_base, version))

    #exemplos
    result_examples = call_llm(build_examples(topic, prompt_base, version))

    #perguntas
    result_question = call_llm(build_questions(topic, prompt_base, version))

    #resumo
    result_resumo = call_llm(build_visual_resumo(topic, prompt_base, version))

    result_data = {
        "timestamp": time_now,
        "prompt_version": version,
        "name": name,
        "topic": topic,
        "profile": {
            "age": age,
            "level": level,
            "howLearning": howLearning
        },
        "outputs": {
            "explicacao": result_explication,
            "exemplos": result_examples,
            "perguntas": result_question,
            "resumo": result_resumo
        }
    }
    return result_data

def verify_profile(name, age, level, howLearning, topic):
    
    #storing user profiles

    data_profiles = load_data("profiles.json", {})

    time_now = datetime.now(timezone.utc).isoformat()
    information = {"age": age, "level": level, "howLearning": howLearning, "last_modified": time_now}

    #stores max 5 different user profiles
    #Nome como ID. Confere se outro perfil com o mesmo nome aparecer, seria uma atualização
    #Caso não esteja armazenado ainda, retira o que foi modificado a mais tempo
    if name not in data_profiles and len(data_profiles) >= 5:
        #remove the oldest based on timestamp
        oldest_time = None
        oldest_name = None
        for n, profile in data_profiles.items():
            time = profile["last_modified"]
            if oldest_time is None or time < oldest_time:
                oldest_time = time
                oldest_name = n
        del data_profiles[oldest_name]

    data_profiles[name] = information #atualização

    if not save_data("profiles.json", data_profiles):
        print("Não foi possivel salvar o Perfil")

def verify_response(name, age, level, howLearning, topic, version):
    time_now = datetime.now(timezone.utc).isoformat()
    #storing responses 
    data_responses = load_data("response_history.json", [])

    #including cache 

    for entry in data_responses:
        if entry["name"] == name and entry["topic"] == topic and entry["profile"]["age"] == age and entry["profile"]["level"] == level and entry["profile"]["howLearning"] == howLearning and entry["prompt_version"] == version:
            #já exixte um resultado gerado para aquele aluno 
            #retorna o resultado ja existente
            return entry["outputs"]
        
    #Caso não esteja no cache, gera nova resposta e salva

    result_data = generate_new_response(name, age, level, howLearning, topic, time_now, version)
    data_responses.append(result_data)
    if not save_data("response_history.json", data_responses):
        print("Não foi possivel salvar a Resposta")
    
    return result_data["outputs"]


def generate_main(name, age, level, howLearning, topic, prompt_option):

    verify_profile(name, age, level, howLearning, topic)

    outputs = {
        "v1": None,
        "v2": None
    }

    if prompt_option == "Compare":
        outputs["v1"] = verify_response(name, age, level, howLearning, topic, "1")
        outputs["v2"] = verify_response(name, age, level, howLearning, topic, "2")

    elif prompt_option == "v1":
        outputs["v1"] = verify_response(name, age, level, howLearning, topic, "1")

    elif prompt_option == "v2":
        outputs["v2"] = verify_response(name, age, level, howLearning, topic, "2")

    return outputs

if __name__ == "__main__":
    app.run(debug=True)

    