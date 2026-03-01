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

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/generate", methods=["POST"])
def generate():
    name = request.form["name"]
    topic = request.form["topic"]
    age = int(request.form["age"])
    level = request.form["level"]
    howLearning = request.form["howLearning"]

    outputs = generate_main(name, age, level, howLearning, topic)

    return render_template("result.html", outputs=outputs)

def generate_main(name, age, level, howLearning, topic):

    #storing user profiles

    if not os.path.exists("profiles.json"):
        data = {}
    else:
        with open('profiles.json', 'r', encoding = 'utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    time_now = datetime.now(timezone.utc).isoformat()
    information = {"age": age, "level": level, "howLearning": howLearning, "last_modified": time_now}

    #stores max 5 different user profiles
    if name in data:
        #conferir se já existe um perfil igual
        #vou usar o nome como ID, ou seja, se outro perfil com o mesmo nome aparecer, seria uma atualização
        data[name] = information
    else:
        if len(data) >= 5:
            #remove the oldest based on timestamp
            oldest_time = None
            oldest_name = None
            for n, profile in data.items():
                time = profile["last_modified"]
                if oldest_time is None or time < oldest_time:
                    oldest_time = time
                    oldest_name = n
            del data[oldest_name]

        data[name] = information

    with open('profiles.json', 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    #storing responses 
    if not os.path.exists("response_history.json"):
        data = []
    else:
        with open('response_history.json', 'r', encoding = 'utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = []

    #including cache 

    for entry in data:
        if entry["name"] == name and entry["topic"] == topic and entry["profile"]["age"] == age and entry["profile"]["level"] == level and entry["profile"]["howLearning"] == howLearning:
            #já exixte um resultado gerado para aquele aluno 
            #retorna o resultado ja existente
            return entry["outputs"]
        
    #ainda não foi gerado

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

    data.append(result_data)
    with open('response_history.json', 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)
    
    return result_data["outputs"]


if __name__ == "__main__":
    app.run(debug=True)

    