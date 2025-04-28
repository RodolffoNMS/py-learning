import pytest
from unittest.mock import patch
from funcionarioComum import FuncionarioComum
from gerente import Gerente
from sistema_rh import SistemaRH

def test_funcionario_comum_calcular_bonus():
    funcionario = FuncionarioComum("Maria", 2000)
    assert funcionario.calcular_bonus() == 200  # 10% de 2000

def test_gerente_calcular_bonus():
    gerente = Gerente("Carlos", 5000, 1000)
    assert gerente.calcular_bonus() == 2000  # 20% de 5000 + 1000

def test_set_salario_negativo():
    funcionario = FuncionarioComum("João", 1000)
    with pytest.raises(ValueError):
        funcionario.set_salario(-500)

def test_mostrar_bonus_log(mocker):
    sistema_rh = SistemaRH()
    funcionario = FuncionarioComum("Ana", 3000)
    sistema_rh.adicionar_funcionario(funcionario)
    
    with mocker.patch('builtins.print') as mock_print:
        sistema_rh.mostrar_bonus(funcionario)
        mock_print.assert_any_call("Mostrando bônus de Ana.")
        mock_print.assert_any_call("Bônus de Ana: 300.0")
        
# Teste
def test_mostrar_bonus_log(mocker):
    sistema_rh = SistemaRH()
    funcionario = FuncionarioComum("Ana", 3000)
    sistema_rh.adicionar_funcionario(funcionario)

    with mocker.patch('builtins.print') as mock_print:
        sistema_rh.mostrar_bonus(funcionario)
        mock_print.assert_any_call("Mostrando bônus de Ana.")
        mock_print.assert_any_call("Bônus de Ana: 600.0")