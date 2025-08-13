def listar_despesas(lista_despesas: list):
    if not lista_despesas:
        print('\n⚠️ Sua lista de despesa está vazia.\n')
    else:
        print("\n📜 Lista de Despesas\n")
        for i, despesa in enumerate(lista_despesas, start=1):
            print(f"{i}. {despesa['descricao']} - Categoria: {despesa['categoria']}")
            print(f"   Valor: R${despesa['valor']:,.2f} - Data: {despesa['data']}")
            print('-' * 40)
