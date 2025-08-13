import os
import pandas as pd

pd.options.display.float_format = 'R${:,.2f}'.format

def relatorio(data_dir: str):
    path = os.path.join(data_dir, 'despesas.csv')

    if not os.path.exists(path) or os.stat(path).st_size == 0:
        print("\n⚠️ Nenhuma despesa registrada para gerar relatório.\n")
        return

    df = pd.read_csv(path)
    
    if df.empty:
        print("\n⚠️ Nenhuma despesa registrada para gerar relatório.\n")
        return

    print("\n📊 Relatório de Despesas\n")
    print(f"Total gasto: R${df['valor'].sum():,.2f}")
    print("Categoria mais cara: ", df.groupby('categoria')['valor'].sum().idxmax())
    print("\nMédia por categoria:\n", df.groupby('categoria')['valor'].mean())
