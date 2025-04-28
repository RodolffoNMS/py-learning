from abc import ABC, abstractmethod

class Funcionario(ABC):
    def __init__(self, nome, salario):
        self.__nome = nome         # Atributo privado
        self.set_salario(salario) # Validar salário com setter

    @abstractmethod
    def calcular_bonus(self):
        pass # Método abstrato

    def get_nome(self): # Retorna nome
        return self.__nome
    
    def get_salario(self):  # Retorna o salário
        return self.__salario

    def set_salario(self, salario): # Atualiza o salário se a validação passar
        if salario < 0:
            raise ValueError('Salario não pode ser negativo')
        self.__salario = salario