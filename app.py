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
    try:
        age = int(request.form["age"])
    except ValueError:
        return "Idade Inválida"
    level = request.form["level"]
    howLearning = request.form["howLearning"]

    outputs = generate_main(name, age, level, howLearning, topic)

    return render_template("result.html", outputs=outputs)


def load_data(path: str, default: any) -> any:
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
    
def generate_new(name: str, age: int,  level: str, howLearning: str, topic: str, time_now: str) -> dict[str, Any]:
    prompt_base = build_prompt_base(name, age, level, howLearning)

    #explicação
    result_explication = call_llm(build_explication(topic, prompt_base))

    #exemplos
    result_examples = call_llm(build_examples(topic, prompt_base))

    #perguntas
    result_question = call_llm(build_questions(topic, prompt_base))

    #resumo
    result_resumo = call_llm(build_visual_resumo(topic, prompt_base))

    result_data = {
        "timestamp": time_now,
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

def generate_main(name, age, level, howLearning, topic):

    #storing user profiles

    data_profiles = load_data("profiles.json", {})

    time_now = datetime.now(timezone.utc).isoformat()
    information = {"age": age, "level": level, "howLearning": howLearning, "last_modified": time_now}

    #stores max 5 different user profiles
    if name in data_profiles:
        #conferir se já existe um perfil igual
        #vou usar o nome como ID, ou seja, se outro perfil com o mesmo nome aparecer, seria uma atualização
        data_profiles[name] = information
    else:
        if len(data_profiles) >= 5:
            #remove the oldest based on timestamp
            oldest_time = None
            oldest_name = None
            for n, profile in data_profiles.items():
                time = profile["last_modified"]
                if oldest_time is None or time < oldest_time:
                    oldest_time = time
                    oldest_name = n
            del data_profiles[oldest_name]

        data_profiles[name] = information

    if not save_data("profiles.json", data_profiles):
        print("Não foi possivel salvar o Perfil")

    #storing responses 
    data_responses = load_data("response_history.json", [])

    #including cache 

    for entry in data_responses:
        if entry["name"] == name and entry["topic"] == topic and entry["profile"]["age"] == age and entry["profile"]["level"] == level and entry["profile"]["howLearning"] == howLearning:
            #já exixte um resultado gerado para aquele aluno 
            #retorna o resultado ja existente
            return entry["outputs"]
        
    #ainda não foi gerado

    result_data = generate_new(name, age, level, howLearning, topic, time_now)
    data_responses.append(result_data)
    if not save_data("response_history.json", data_responses):
        print("Não foi possivel salvar a Resposta")
    
    return result_data["outputs"]


if __name__ == "__main__":
    app.run(debug=True)

    