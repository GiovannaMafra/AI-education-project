# AI Personalized Education Project

Uma plataforma inteligente desenvolvida para o **Desafio Técnico de Estágio em IA e Engenharia de Prompt**. O sistema utiliza modelos de linguagem de última geração (Google Gemini) para gerar materiais educativos altamente personalizados, adaptando a linguagem, a complexidade e o estilo visual conforme o perfil de cada aluno.

🔗 **Acesse a aplicação online:** [https://ai-education-project.onrender.com](https://ai-education-project.onrender.com)

---

## Funcionalidades Principais

* **Perfil de Aluno Dinâmico:** Customização baseada em nome, idade, nível (iniciante a avançado) e estilo de aprendizado (visual, auditivo, etc.).
* **Motor de Prompt Otimizado:** Implementação de técnicas de **Chain-of-Thought**, **Persona Prompting**, entre outras, para garantir clareza pedagógica.
* **Sistema de Comparação:** Permite gerar e comparar o conteúdo entre uma versão direta (v1) e uma versão otimizada com técnicas avançadas (v2).
* **4 Pilares Educativos:** Explicação conceitual, exemplos práticos contextualizados, perguntas de reflexão e resumo visual em ASCII.
* **Sistema de Cache Inteligente:** Para otimizar performance e custos, a aplicação consulta o arquivo `response_history.json`. Se o mesmo perfil solicitar o mesmo tópico, a resposta é recuperada do cache local sem novas chamadas à API.
* **Interface Web Moderna:** Desenvolvida em Flask com renderização em tempo real de Markdown via `Marked.js`.

## Stack Técnica

* **Backend:** Python 3.10+ e Flask.
* **IA:** Google Gemini API (via biblioteca `requests`).
* **Frontend:** HTML5, CSS3, JavaScript e `Marked.js`.
* **Persistência:** JSON (armazenamento de histórico e cache).
* **Deploy:** Render.

---

## Instalação e Execução Local

Siga os passos abaixo para rodar o projeto em sua máquina:

### 1️⃣ Configurar Variáveis de Ambiente (Obrigatório)

Por questões de segurança, as chaves de API não são enviadas ao repositório.

1. Na raiz do projeto, localize o arquivo `.env.example`.
2. Renomeie-o para `.env`.
3. Adicione sua chave de API do Gemini:

```env
GEMINI_API_KEY=SUA_CHAVE_AQUI
```

---

### 3️⃣ Instalar Dependências

```bash
#Recomendado usar ambiente virtual (venv)
python -m venv venv

#Linux / Mac
source venv/bin/activate

#Windows
venv\Scripts\activate

pip install -r requirements.txt
```

---

### 4️⃣ Executar a Aplicação

```bash
python app.py
```
---

## Observações

- **Importante (Deploy no Render - plano gratuito):** No plano gratuito do Render, o sistema de arquivos é efêmero. Isso significa que, após reinicializações do servidor (que podem ocorrer automaticamente por inatividade), o arquivo `responde_history.json` pode ser limpo. Nesses casos, uma requisição já realizada anteriormente poderá não ser encontrada no cache, gerando uma nova chamada à API. Essa limitação está relacionada à infraestrutura do ambiente gratuito, e não à lógica do sistema de cache implementado na aplicação.
