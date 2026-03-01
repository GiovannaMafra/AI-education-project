from llm.user import call_llm
from prompt_engine.builder import build_prompt_base
from prompt_engine.builder import build_explication
from prompt_engine.builder import build_examples
from prompt_engine.builder import build_questions
from prompt_engine.builder import build_visual_resumo
from prompt_engine.mock import Mock

def main():
    topic = input("Digite o assunto: ")
    name = input("Digite seu nome: ")
    age = input("Digite sua idade: ")
    level = input("Digite seu nivel: ")
    howLearning = input("Digite seu estilo de aprendizado: ")

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

    