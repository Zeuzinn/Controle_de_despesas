from datetime import datetime
from core.persistencia import salvar_csv


def registrar_despesa(lista_despesas: list, data_dir: str):
    dados = _coletar_despesas()
    if dados is None:
        return

    descricao, categoria, valor, data = dados

    lista_despesas.append({'descricao': descricao, 'categoria': categoria, 'valor': valor, 'data': data})
    salvar_csv(lista_despesas, 'despesas.csv', data_dir)
    print('\n✅ Despesa registrada com sucesso!\n')


def _coletar_despesas():
    descricao = input('Descrição: ').title().strip()
    if not descricao:
        print('\n❌ A descrição não pode ficar em branco.\n')
        return
    
    categoria = input('Categoria: ').title().strip()
    if not categoria:
        print('\n❌ A categoria não pode ficar em branco.\n')
        return
    
    try:
        valor_str = input('Valor (R$): ')
        valor_str = valor_str.replace(',', '.')
        valor = float(valor_str)
    
        if valor < 0:
            print('\n⚠️ O valor não pode ser negativo\n')
            return
    
    except ValueError:
        print('\n❌ Digite apenas número\n')
        return

    data = datetime.now().strftime('%Y-%m-%d')

    return descricao, categoria, valor, data
