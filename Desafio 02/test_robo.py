import pytest
from RoboExplorador import RoboExplorador
from RelatorioDeMissao import RelatorioDeMissao

def test_robo_explorador_diferente():
    robo = RoboExplorador("LunarLander", "Saturno", 60)
    assert str(robo) == "Robô LunarLander - Destino: Saturno - Energia: 60%"

def test_resumo_diferente():
    relatorio = RelatorioDeMissao("LunarLander", "Saturno", 60, (("anéis", 7), ("vento", 12.3)))
    assert relatorio.resumo() == ["anéis: 7", "vento: 12.3"]

def test_contagem_leituras_diferente():
    relatorio = RelatorioDeMissao("LunarLander", "Saturno", 60, (("anéis", 7), ("vento", 12.3), ("pressão", 95)))
    assert relatorio.contagem_leituras() == 3

def test_resumo_vazio():
    relatorio = RelatorioDeMissao("NebulaNavigator", "Netuno", 90, ())
    assert relatorio.resumo() == []

def test_contagem_leituras_vazio():
    relatorio = RelatorioDeMissao("NebulaNavigator", "Netuno", 90, ())
    assert relatorio.contagem_leituras() == 0
    
def test_robo_explorador(): 
    robo = RoboExplorador("AstroBot", "Júpiter", 75)
    assert str(robo) == "Robô AstroBot - Destino: Júpiter - Energia: 75%"

def test_relatorio_de_missao_heranca():
    relatorio = RelatorioDeMissao("AstroBot", "Júpiter", 75, (("gravidade", 24.79), ("tempestade", 8.0)))
    assert isinstance(relatorio, RoboExplorador)

def test_resumo():
    relatorio = RelatorioDeMissao("AstroBot", "Júpiter", 75, (("gravidade", 24.79), ("tempestade", 8.0)))
    assert relatorio.resumo() == ["gravidade: 24.79", "tempestade: 8.0"]

def test_contagem_leituras():
    relatorio = RelatorioDeMissao("AstroBot", "Júpiter", 75, (("gravidade", 24.79), ("tempestade", 8.0)))
    assert relatorio.contagem_leituras() == 2