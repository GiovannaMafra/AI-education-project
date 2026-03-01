def build_prompt_base(name: str, age: int,  level: str, howLearning: str) -> str:

    #persona prompting
    persona =  "Você é um professor experiente em Pedagogia, especialista em ensinar de forma clara e adaptada para cada aluno."

    #context setting 
    context = f"Você está ensinando para {name}, que tem {age} e que tem o nível de conhecimento {level} no assunto e prefere aprender de forma {howLearning}."

    #formatting
    format = "Organize todas as respostas com títulos claros, subtítulos e listas numeradas quando necessário."
    
    return persona + "\n" + context + "\n" + format

def build_explication(topic: str, base: str) -> str:

    #chain-of-thought
    steps = (
        f"Explique o tema {topic} passo a passo,organizando o raciocínio em etapas claras. Seja didático, organizado e adapte exemplos ao estilo de aprendizado do aluno."
    )

    return base + "\n" + steps

def build_examples(topic: str, base: str) -> str:
    instructions = f"Forneça 3 exemplos práticos sobre {topic}. Explique cada exemplo passo a passo. Relacione com situações do cotidiano do aluno."

    return base + "\n" + instructions

def build_questions(topic: str, base: str) -> str:
    instructions = f"Crie 5 perguntas sobre o tema {topic}. Inclua 3 perguntas objetivas e 2 discursivas. inclua gabarito no final. Adapte as perguntas para o contexto  do aluno."

    return base + "\n" + instructions

def build_visual_resumo(topic: str, base: str) -> str:
    instructions = f"Resuma o tema {topic} de forma clara, objetiva e simples. Seja direto e adapte para o contexto do aluno."

    return base + "\n" + instructions