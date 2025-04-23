class Transacao:
    
    def __init__(self, descricao, valor, categoria, data):
        self.descricao = descricao
        self.valor = valor
        self.categoria = categoria
        self.data = data 
    
    def resumo(self):
        valor_formatado = f"{'+' if self.valor >= 0 else ''}{self.valor:.2f}"
        return f"{self.descricao} | {valor_formatado} | {self.categoria} | {self.data}"

