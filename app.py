from llm.user import call_llm
from prompt_engine.builder import build_prompt
from prompt_engine.mock import Mock
import json

def main():
    topic = input("Digite o assunto: ")
    name = input("Digite seu nome: ")
    age = input("Digite sua idade: ")
    level = input("Digite seu nivel: ")
    howLearning = input("Digite seu estilo de aprendizado: ")

    #storing user profiles
    with open('profiles.json', 'r', encoding = 'utf-8') as file:
        data = json.load(file)

    information = {"age": age, "level": level, "howLearning": howLearning}

    #stores max 5 different user profiles
    if name in data:
        #conferir se já existe um perfil igual
        #DUVIDA: Perfis diferentes seriam nomes diferentes? se aparecer o mesmo nome, eu atualizo o perfil ou crio um novo?
        if data[name] != information:
            #atualiza o perfil
            data[name] = information
    else:
        if len(data) >= 5:
            #remove the oldest one
            oldest_key = next(iter(data))
            del data[oldest_key]

        data[name] = information

    with open('profiles.json', 'w', encoding= 'utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

    
    prompt = build_prompt(topic, name, age, level, howLearning)
    
    #mock = Mock()
    #result = mock.generate(prompt)

    result = call_llm(prompt)

    print("\nResposta:\n")
    print(result)

if __name__ == "__main__":
    main()

    