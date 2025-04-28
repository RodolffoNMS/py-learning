from funcionarioComum import FuncionarioComum
from gerente import Gerente

def logar_acao(func):
    def wrapper(*args, **kwargs):  # Aceita múltiplos argumentos e palavras-chave
        funcionario = args[0]  # O primeiro argumento é o funcionario
        print(f"Mostrando bônus de {funcionario.get_nome()}.")
        return func(*args, **kwargs)  # Chama a função original com todos os argumentos
    return wrapper

class SistemaRH:
    def __init__(self):
        self.funcionarios = []

    def adicionar_funcionario(self, funcionario):
        self.funcionarios.append(funcionario)

    @logar_acao
    def mostrar_bonus(self, funcionario):
        bonus = funcionario.calcular_bonus()
        print(f"Bônus de {funcionario.get_nome()}: {bonus}")

