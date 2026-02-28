def build_prompt(topic: str, name: str, age: int,  level: str, howLearning: str) -> str:

    #persona prompting
    persona =  "Você é um professor experiente em Pedagogia, especialista em ensinar de forma clara e adaptada para cada aluno."

    #context setting 
    context = f"Você está ensinando para {name}, que tem {age} e que tem o nivel de conhecimento {level} no assunto e prefere aprender de forma {howLearning}."

    #chain-of-thought
    steps = (
        "Explique o tema passo a passo, como se estivesse pensando em voz alta. "
        "Seja didático, organizado e adapte exemplos ao estilo de aprendizado do aluno. "
        "Use uma linguagem adequada ao nível de conhecimento do aluno."
    )

    #output
    output = (
        "Formate a resposta da seguinte forma:\n"
        "1. Definição do conceito\n"
        "2. Explicação detalhada\n"
        "3. Exemplos\n"
        "4. Conclusão\n"
    )

    #levels
    level = level.lower()
    if level == "iniciante":
        level_instructions = f"Explique o tema de forma simples e linguagem facil: tema: {topic}"

    elif level == "intermediario":
        level_instructions =  f"Explique o tema para alguem que tem conhecimento intermediario no assunto, didatico e organizado: tema: {topic}"

    elif level == "avançado":
        level_instructions =  f"Explique o seguinte tema de forma mais avançada, com conceitos tecnicos e detalhes importantes: tema: {topic}"

    else:
        level_instructions =  f"Explique o seguinte tema: {topic}"
    
    #construção
    prompt = (
        f"{persona}\n"
        f"{context}\n"
        f"{steps}\n"
        f"{level_instructions}\n"
        f"{output}\n"
        f"Tema: {topic}"
    )

    return prompt