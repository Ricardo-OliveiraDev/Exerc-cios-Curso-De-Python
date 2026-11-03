menor_preco = total = maior_1000 = 0
nome_menor = ""
while True:
    produto = input("Digite o nome do produto: ")
    preco = float(input("Digite o valor do produto: R$"))
    if preco > menor_preco == 0:
        menor_preco = preco
        nome_menor = produto
    total += preco
    if preco > 1000:
        maior_1000 += 1
    if preco < menor_preco:
        menor_preco = preco
        nome_menor = produto
    resposta = input("Deseja continuar? [S/N]").strip().lower()[0]
    if resposta == "n":
        break
print(f"{"FIM DO PROGRAMA":-^30}")
print(f"""O total da sua compra foi de R${total:.2f}
temos {maior_1000} produtos que custam mais de R$1000 reais
o produto mais barato foi {nome_menor} que custa R${menor_preco:.2}""")
