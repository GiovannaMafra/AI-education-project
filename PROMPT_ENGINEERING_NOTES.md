# Prompt Engineering Notes

Este documento detalha as estratégias, técnicas e decisões pedagógicas utilizadas no desenvolvimento do motor de geração de conteúdo desta plataforma.

## 1. Arquitetura dos Prompts
A aplicação utiliza uma estrutura de **Prompt Composto**, onde cada instrução é montada dinamicamente através do `builder.py`. A lógica é dividida em:

* **Prompt Base (`build_prompt_base`):** Estabelece a fundação com **Persona Prompting** (Professor Experiente), **Context Setting** (dados específicos do aluno) e **Formatting Rules** (Markdown estrito e blocos de código para ASCII).
* **Camada de Tarefa Especializada:** Quatro funções distintas que injetam instruções específicas para Explicação, Exemplos, Perguntas e Resumo Visual, evitando a sobrecarga de contexto e garantindo foco em cada tipo de conteúdo.

---

## 2. Técnicas Avançadas Implementadas

### A. Persona Prompting & Context Setting
Ao definir a IA como um *"Professor experiente em Pedagogia"*, o modelo assume um tom de voz adequado. A inclusão sistemática das variáveis `{name}`, `{age}`, `{level}` e `{howLearning}` permite que a LLM ajuste automaticamente a complexidade do vocabulário e o tipo de analogia utilizada.

### B. Chain-of-Thought (Cadeia de Pensamento) - Aplicado na v2
Na versão 2 da **Explicação**, implementamos o raciocínio encadeado. Em vez de apenas definir o tema, forçamos o modelo a:
1. Conectar o conceito ao cotidiano.
2. Desenvolver o raciocínio em etapas progressivas.
3. Aplicar analogias baseadas no estilo de aprendizado.
Isso reduz drasticamente a chance de explicações genéricas e superficiais.

### C. Taxonomia de Bloom - Aplicado na v2
Na geração de **Perguntas**, a v2 utiliza a Taxonomia de Bloom para garantir que o aluno não apenas decore, mas processe a informação em diferentes níveis cognitivos:
* **Lembrança e Compreensão:** Fatos e conceitos.
* **Aplicação e Análise:** Problemas práticos e comparação de erros.
* **Síntese:** Criação e reflexão profunda.

### D. Estruturação de Saída Visual (ASCII Art)
Para o **Resumo Visual**, o prompt v2 utiliza restrições de formatação para garantir a integridade dos diagramas em dispositivos diferentes. O uso de "Metáfora do Objeto" na v2 auxilia na ancoragem da memória de longo prazo através de associações visuais/mentais.

---

## 3. Comparativo de Versões (v1 vs v2)

| Recurso | Versão 1 (Baseline) | Versão 2 (Avançada/Otimizada) |
| :--- | :--- | :--- |
| **Estratégia** | Instruções diretas e simples. | Uso de frameworks pedagógicos (Bloom/CoT). |
| **Explicação** | Passo a passo didático padrão. | Conexão cotidiana + Progressão encadeada. |
| **Exemplos** | 3 exemplos cotidianos. | 3 níveis de dificuldade (Básico, Intermediário, Avançado). |
| **Perguntas** | Mix de objetivas e discursivas. | Escalonamento por níveis cognitivos de Bloom. |
| **Visual** | Sugestão de diagrama ASCII simples. | Mapa mental estruturado + Glossário em boxes. |

---

## 4. Mitigação de Alucinações
* **Ancoragem em Erros Comuns:** Ao solicitar que a IA "aponte e corrija um erro comum", forçamos o modelo a validar a lógica correta contra a incorreta, aumentando a precisão técnica da resposta.

---