from core.menu import menu
from core.registro import registrar_despesa
from core.listagem import listar_despesas
from core.relatorio import relatorio
from core.remover import remover_despesa
from core.persistencia import carregar_csv, salvar_csv
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.path.join(BASE_DIR, 'data')


def main():
    lista_despesas = carregar_csv('despesas.csv', DATA_DIR)

    while True:
        menu()
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            registrar_despesa(lista_despesas, DATA_DIR)
        elif opcao == '2':
            listar_despesas(lista_despesas)
        elif opcao == '3':
            relatorio(DATA_DIR)
        elif opcao == '4':
            remover_despesa(lista_despesas, DATA_DIR)
        elif opcao == '0':
            print("💾 Salvando dados e saindo...")
            salvar_csv(lista_despesas, 'despesas.csv', DATA_DIR)
            break
        else:
            print("❌ Opção inválida!")

if __name__ == "__main__":
    main()
    