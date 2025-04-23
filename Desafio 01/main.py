from modelos.transacao import Transacao
from modelos.carteira import Carteira

def main():
    # Criação da carteira
    carteira = Carteira()

    # Adicionando
    carteira.adicionar(Transacao("Salário", 5000, "Renda", "2023-10-01"))
    carteira.adicionar(Transacao("Aluguel", -1500, "Despesa", "2023-10-02"))
    carteira.adicionar(Transacao("Supermercado", -300, "Despesa", "2023-10-03"))
    carteira.adicionar(Transacao("Venda de produtos", 200, "Renda", "2023-10-04"))

    carteira.exibir_transacoes()
    carteira.resumo_geral()
    
if __name__ == "__main__":
    main()