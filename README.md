# 💰 Controle de Despesas

Sistema simples e prático para controle de despesas, feito em Python. Ideal para gerenciar gastos pessoais, de pequenas lojas ou restaurantes, direto do terminal.



---

## 🧠 Funcionalidades

- ✅ Registrar novas despesas (com descrição, categoria, valor e data)
- 📜 Listar todas as despesas salvas
- 📊 Gerar relatório financeiro com:
  - Total gasto
  - Categoria mais cara
  - Média por categoria
- 🗑️ Remover despesas por índice
- 💾 Persistência de dados automática via arquivos `.csv`

---

## 📂 Estrutura do Projeto

```
Controle_de_despesas/
│
├── app.py # Arquivo principal
├── core/
│ ├── menu.py               # Menu principal do sistema
│ ├── registro.py           # Registro de novas despesas
│ ├── listagem.py           # Listagem de despesas
│ ├── relatorio.py          # Geração de relatório
│ ├── remover.py            # Remoção de despesas
│ └── persistencia.py       # Leitura e escrita em CSV
│
└── data/
└── despesas.csv            # Armazena os dados persistidos
```
---

## ▶️ Como Executar

1. **Clone o repositório**:

```bash
git clone https://github.com/Zeuzinn/Controle_de_despesas.git
cd Controle_de_despesas
```

2. **Crie um ambiente virtual (opcional, mas recomendado):**
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\\Scripts\\activate   # Windows
```

3. **Instale as dependências:**
```
pip install -r requirements.txt
```

📦 **Requisitos:**

- Python 3.7+
- pandas (para geração de relatórios)

4. **Execute o programa:**

```bash
python app.py
```

## 📄 Licença

Este projeto está licenciado sob a Licença MIT.  
Veja o arquivo [LICENSE](./LICENSE) para mais detalhes.
