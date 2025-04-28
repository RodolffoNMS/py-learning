from funcionarioComum import Funcionario

class Gerente(Funcionario):
    def __init__(self, nome, salario, bonus_adicional):
        super().__init__(nome, salario)  # Chama o construtor da classe pai
        self.bonus_adicional = bonus_adicional  # Inicializa o atributo extra

    def calcular_bonus(self):
        # Retorna 20% do salário mais o bônus adicional
        return (self.get_salario() * 0.20) + self.bonus_adicional