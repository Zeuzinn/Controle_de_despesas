from core.listagem import listar_despesas
from core.persistencia import salvar_csv

def remover_despesa(lista_despesas: list, data_dir: str):
    listar_despesas(lista_despesas)
    try:
        indice = int(input("Digite o número da despesa que deseja remover: "))
        if 1 <= indice <= len(lista_despesas):
            removida = lista_despesas.pop(indice - 1)
            salvar_csv(lista_despesas, 'despesas.csv', data_dir)
            print(f"\n🗑️ Despesa '{removida['descricao']}' removida com sucesso!\n")
        else:
            print("\n❌ Índice inválido.\n")
    except ValueError:
        print("\n❌ Digite um número válido.\n")
