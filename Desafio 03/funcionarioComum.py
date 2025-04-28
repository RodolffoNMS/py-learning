from funcionarios import Funcionario

class FuncionarioComum(Funcionario):
    def __init__(self, nome, salario):
        super().__init__(nome, salario)  # Chama o construtor da classe pai

    def calcular_bonus(self):
        return self.get_salario() * 0.10  # Retorna 10% do salário