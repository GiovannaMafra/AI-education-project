#from llm.user import call_llm
from prompt_engine.builder import build_prompt
from prompt_engine.mock import Mock

def main():
    topic = input("Digite o assunto: ")
    name = input("Digite seu nome: ")
    age = input("Digite sua idade: ")
    level = input("Digite seu nivel: ")
    howLearning = input("Digite seu estilo de aprendizado: ")

    prompt = build_prompt(topic, name, age, level, howLearning)
    mock = Mock()
    result = mock.generate(prompt)
    print("\nResposta:\n")
    print(result)

if __name__ == "__main__":
    main()

    