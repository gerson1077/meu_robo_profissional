import datetime
import pandas as pd

#simulação de coleta de dados
def coletar_dados():
    return[
        {
            "data": datetime.date.today(),
            "evento": "Processamento finalizado",
            "status": "OK"},
    ]
    
#salvar em um CSV
def salvar_relatorio(dados):
    df = pd.DataFrame(dados)
    df.to_csv("dados/relatorio.csv", index=False, encoding="utf-8")
    print("Relatório salvo em dados/relatorio.csv")
    
#execução principal
if __name__ == "__main__":
    print("Iniciando Robô...")
    dados = coletar_dados()
    salvar_relatorio(dados)
    print("Coleta de dados e geração de relatório concluídas.")
