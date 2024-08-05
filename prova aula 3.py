dicionario = {}
contador = 0

def adicionar_produto(nome, preco):
    dicionario[nome] = preco

for i in range(5):
    nome = input(f'Digite o nome do produto {i+1}: ')
    preco = float(input(f'Digite o preço do produto {i+1}: '))
    adicionar_produto(nome, preco)
    contador += preco

print(f'O dicionário ficou assim: {dicionario}')
print(f'A soma de tudo ficou assim: {contador}')