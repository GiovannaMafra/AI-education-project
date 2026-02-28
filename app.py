from llm.user import call_llm

def main():
    topic = input("Digite o assunto: ")
    result = call_llm(f"Explique de forma simples e breve o que é {topic}.")
    print("\nResposta:\n")
    print(result)

if __name__ == "__main__":
    main()

    