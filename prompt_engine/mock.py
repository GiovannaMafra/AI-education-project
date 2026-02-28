#como a chave da api ainda não está funcionando farei um mock para conseguir progredir com o projeto

class Mock:
    def generate(self, prompt: str) -> str:
        return f"[MOCK] retorna a resposta para o {prompt}"