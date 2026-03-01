from llm.user import call_llm
from prompt_engine.builder import build_prompt_base
from prompt_engine.builder import build_explication
from prompt_engine.builder import build_examples
from prompt_engine.builder import build_questions
from prompt_engine.builder import build_visual_resumo
from prompt_engine.mock import Mock
import json
from datetime import datetime
import os

def main():
    topic = input("Digite o assunto: ")
    name = input("Digite seu nome: ")
    age = int(input("Digite sua idade: "))
    level = input("Digite seu nivel (iniciante, intermediario ou avançado): ")
    while (level != "iniciante" and level != "intermediario" and level != "avançado"):
        level = input("Digite nivel válido (iniciante, intermediario ou avançado): ")
    howLearning = input("Digite seu estilo de aprendizado: ")
    while (howLearning != "visual" and howLearning != "auditivo" and howLearning != "leitura-escrita" and howLearning != "cinestésico"):
        howLearning = input("Digite um estilo válido (visual, auditivo, leitura-escrita ou cinestésico): ")

    #storing user profiles

    if not os.path.exists("profiles.json"):
        data = {}
    else:
        with open('profiles.json', 'r', encoding = 'utf-8') as file:
            try:
                data = json.load(file)
            except json.JSONDecodeError:
                data = {}

    time_now = datetime.now(datetime.timezone.utc).isoformat()
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

    
    prompt_base = build_prompt_base(name, age, level, howLearning)

    #explicação
    result_explication = call_llm(build_explication(topic, prompt_base))
    #adicionar a resposta no json?

    #exemplos
    result_examples = call_llm(build_examples(topic, prompt_base))

    #perguntas
    result_question = call_llm(build_questions(topic, prompt_base))

    #resumo
    result_resumo = call_llm(build_visual_resumo(topic, prompt_base))

    #mock = Mock()
    #result = mock.generate(prompt)

    result_data = {
        "explicacao": result_explication,
        "exemplos": result_examples,
        "perguntas": result_question,
        "resumo": result_resumo
    }

    #print("\nResposta:\n")
    #print(result)

if __name__ == "__main__":
    main()

    