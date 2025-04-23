from modelos.transacao import Transacao

class Carteira:
    def __init__(self):
        self.transacoes = []
    
    def adicionar(self, transacao):
        self.transacoes.append(transacao)
    
    def exibir_transacoes(self):
        for transacao in self.transacoes:
            print(transacao.resumo())

    def saldo(self):
        return sum(transacao.valor for transacao in self.transacoes)
    
    def filtrar_por_categoria(self, categoria):
        transacoes_filtradas = [t for t in self.transacoes if t.categoria == categoria]
        for transacao in transacoes_filtradas:
            print(transacao.resumo())
    
    def gastos_totais(self):
        return sum(t.valor for t in self.transacoes if t.valor < 0)

    def renda_total(self):
        return sum(t.valor for t in self.transacoes if t.valor > 0)
    
    def resumo_geral(self):
        total_transacoes = len(self.transacoes)
        renda = self.renda_total()
        gastos = self.gastos_totais()
        saldo_final = self.saldo()
        print("Resumo Geral:")
        print(f"Total de transações: {total_transacoes}")
        print(f"Renda total: {renda:.2f}")
        print(f"Gastos totais: {gastos:.2f}")
        print(f"Saldo final: {saldo_final:.2f}")