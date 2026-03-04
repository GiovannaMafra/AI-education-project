def build_prompt_base(name: str, age: int,  level: str, howLearning: str) -> str:

    #persona prompting
    persona =  "Você é um professor experiente em Pedagogia, especialista em ensinar de forma clara e adaptada para cada aluno."

    #context setting 
    context = f"Você está ensinando para {name}, que tem {age} e que tem o nível de conhecimento {level} no assunto e prefere aprender de forma {howLearning}."

    #formatting
    format = "Regras de formatação obrigatórias:\n"
    "- Use Markdown estrito.\n"
    "- Use '#' para títulos principais e '##' para subtítulos.\n"
    "- Use '**texto**' para negrito em termos importantes.\n"
    "- Use '---' para criar linhas horizontais separando as seções.\n"
    "- Pule uma linha entre parágrafos e itens de lista.\n"
    "- Para o resumo visual, use blocos de código (```) para manter o alinhamento do ASCII."
    
    return persona + "\n" + context + "\n" + format

def build_explication(topic: str, base: str, version: str) -> str:

    if version == "1":
        steps = (f"Explique o tema {topic} passo a passo,organizando o raciocínio em etapas claras. Seja didático, organizado e adapte exemplos ao estilo de aprendizado do aluno.")
    else:
        #chain-of-thought
        steps = (
            f"Desenvolva uma explicação profunda sobre {topic} seguindo rigorosamente estes passos:\n"
            "1. Conecte o conceito ao cotidiano da idade do aluno.\n"
            "2. Desenvolva o raciocínio em etapas progressivas e encadeadas.\n"
            "3. Inclua uma analogia alinhada ao estilo de aprendizado.\n"
            "4. Aponte e corrija um erro comum.\n"
            "5. Conclua com uma síntese prática em até 3 linhas."
        )

    return base + "\n" + steps

def build_examples(topic: str, base: str, version: str) -> str:
    if version == "1":
        instructions = f"Forneça 3 exemplos práticos sobre {topic}. Explique cada exemplo passo a passo. Relacione com situações do cotidiano do aluno."
    else:
        instructions = f"Gere 3 cenários práticos para o tópico '{topic}' com dificuldade progressiva:\n\n"
        "1. Nível básico: exemplo cotidiano, concreto e intuitivo.\n"
        "2. Nível intermediário: exija a combinação de duas ideias do tópico.\n"
        "3. Nível avançado: aplicação em um problema real.\n\n"
        "Para cada cenário, inclua:\n"
        "- Contexto adaptado à idade e ao estilo de aprendizado do aluno.\n"
        "- Raciocínio passo a passo para compreender ou resolver.\n"
        "- Um erro comum relacionado e sua correção."

    return base + "\n" + instructions

def build_questions(topic: str, base: str, version: str) -> str:
    if version == "1":
        instructions = f"Crie 5 perguntas sobre o tema {topic}. Inclua 3 perguntas objetivas e 2 discursivas. inclua gabarito no final."
    else:
        instructions =  f"Gere 5 questões sobre '{topic}' distribuídas segundo a Taxonomia de Bloom:\n"
        "1. Lembrança: pergunta objetiva sobre um conceito fundamental.\n"
        "2. Compreensão: peça explicação do 'porquê' com as próprias palavras.\n"
        "3. Aplicação: apresente um cenário prático.\n"
        "4. Análise: solicite comparação ou identificação de erro conceitual.\n"
        "5. Síntese: questão aberta que exija construção de solução ou reflexão.\n\n"
        "Para cada questão:\n"
        "- Indique o nível cognitivo correspondente.\n"
        "- Forneça gabarito comentado com breve orientação para o raciocínio.\n"
        "- Adapte a linguagem ao nível e contexto do aluno."

    return base + "\n" + instructions

def build_visual_resumo(topic: str, base: str, version: str) -> str:
    if version == "1":
        instructions = f"Resuma o tema {topic} de forma clara, objetiva e simples. Seja direto e adapte para o contexto do aluno. Sugestão de diagrama/mapa mental em ASCII."
    else:
        instructions = f"Crie um resumo de alto impacto visual sobre '{topic}' adpatado para a forma de aprendizado do aluno.\n"
        "1. Mapa mental ASCII: Construa um mapa usando símbolos (ex: ┌─, ├─, │, └─). O mapa deve ter o tópico central e pelo menos 3 ramificações de conceitos-chave.\n"
        "2. Gloassário visual: Escolha os 3 termos mais importantes e coloque-os em [BOXES] com uma explicação de uma única linha ao lado.\n"
        "3. A metáfora do objeto: Descreva o conceito como se fosse um objeto físico ou sistema "
        "conhecido (ex: 'A internet é como um sistema de correios onde...') para facilitar a memorização.\n\n"
        "REGRAS DE FORMATAÇÃO: Use espaçamento correto para que o ASCII não quebre e garanta que a complexidade da linguagem esteja no nível de conhecimento do aluno."

    return base + "\n" + instructions