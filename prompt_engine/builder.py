def build_prompt_base(name: str, age: int,  level: str, howLearning: str) -> str:

    #persona prompting
    persona =  "Você é um professor experiente em Pedagogia, especialista em ensinar de forma clara e adaptada para cada aluno."

    #context setting 
    context = f"Você está ensinando para {name}, que tem {age} e que tem o nivel de conhecimento {level} no assunto e prefere aprender de forma {howLearning}."

    return persona + "\n" + context

def build_explication(topic: str, base: str) -> str:

    #chain-of-thought
    steps = (
        "Explique o tema {topic} passo a passo,organizando o raciocínio em etapas claras. "
        "Seja didático, organizado e adapte exemplos ao estilo de aprendizado do aluno. "
        "Use uma linguagem adequada ao nível de conhecimento do aluno."
    )

    return base + "\n" + steps

def build_examples(topic: str, base: str) -> str:
    instructions = f"Forneça 3 exemplos práticos sobre {topic}. Explique cada exemplo passo a passo. Relacione com situações do cotidiano do aluno."

    return base + "\n" + instructions

def build_questions(topic: str, base: str) -> str:
    instructions = f"Crie 5 perguntas sobre o tema {topic}. Sendo 3 perguntas objetivas e 2 discursivas. inclua gabarito no final. Adapte as perguntas para o contexto  do aluno."

    return base + "\n" + instructions

def build_visual_resumo(topic: str, base: str) -> str:
    instructions = f"Resuma o tema {topic} de forma clara, objetiva e simples. Seja direto e adapte para o contexo do aluno."

    return base + "\n" + instructions