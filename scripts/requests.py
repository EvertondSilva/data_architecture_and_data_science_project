import requests
import pandas as pd

# Definir o produto a ser pesquisado
produto = "notebook"

# URL da API do Mercado Livre
url = f"https://api.mercadolibre.com/sites/MLB/search?q={produto}"

# Fazer a requisição
response = requests.get(url)
dados = response.json()

# Extrair informações dos produtos
produtos = []
for item in dados['results'][:10]:  # Pegamos os 10 primeiros resultados
    produtos.append({
        "id": item["id"],
        "titulo": item["title"],
        "preco": item["price"],
        "condicao": item["condition"],
        "vendedor": item["seller"]["id"],
        "permalink": item["permalink"]
    })

# Criar um DataFrame com os dados
df = pd.DataFrame(produtos)

# Mostrar os primeiros resultados
print(df)
