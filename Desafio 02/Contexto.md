# Parte 1: Classe RoboExplorador
## Crie uma classe chamada RoboExplorador com os seguintes atributos:
- nome: uma string com o nome do robô.
- planeta_destino: uma string com o nome do planeta onde o robô vai trabalhar.
- energia: um número inteiro de 0 a 100 representando a energia restante do robô.
- Crie também um método chamado __str__, que retorna uma frase como esta:
> "Robô Xablau - Destino: Marte - Energia: 87%"
# Parte 2: Classe RelatorioDeMissao (herança)
## Crie uma nova classe chamada RelatorioDeMissao, que herda da classe RoboExplorador.
- Adicione um novo atributo chamado leituras, que deve ser uma tupla de tuplas. Cada tupla interna deve ter dois valores:
    - O tipo do dado coletado (como "temperatura" ou "radiação")
    - O valor coletado (como -50 ou 2.5)
###  **Exemplo de leituras:**
```py
(
    # O código deve retornar da forma como está abaixo:

    ("temperatura", -50),
    ("radiação", 2.5),
)
```

- Implemente dois métodos:
    - resumo: deve retornar uma lista de frases com o nome do dado e o valor. Exemplo:

```py
["temperatura: -50", "radiação: 2.5"]
# contagem_leituras: deve retornar o número total de leituras feitas.
```
## Parte 3: Testes com pytest
- Use a biblioteca pytest para verificar:
- Se a classe RoboExplorador funciona corretamente.
- Se a classe RelatorioDeMissao herda corretamente da classe RoboExplorador.
- Se os métodos resumo e contagem_leituras funcionam e retornam o esperado.
