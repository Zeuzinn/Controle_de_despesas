import os
import csv


def salvar_csv(lista_despesas, nome_arquivo, data_dir):
    os.makedirs(data_dir, exist_ok=True)
    path = os.path.join(data_dir, nome_arquivo)

    with open(path, 'w', newline='', encoding='utf-8') as arquivo:
        escritor = csv.DictWriter(arquivo, fieldnames=['descricao', 'categoria', 'valor', 'data'])
        escritor.writeheader()
        escritor.writerows(lista_despesas)


def carregar_csv(nome_arquivo, data_dir):
    path = os.path.join(data_dir, nome_arquivo)

    if not os.path.exists(path):
        return []
    
    with open(path, 'r', newline='', encoding='utf-8') as arquivo:
        leitor = csv.DictReader(arquivo)
        
        return [
            {'descricao': linha['descricao'],
             'categoria': linha['categoria'],
             'valor': float(linha['valor']),
             'data': linha['data']}
            for linha in leitor
        ]
