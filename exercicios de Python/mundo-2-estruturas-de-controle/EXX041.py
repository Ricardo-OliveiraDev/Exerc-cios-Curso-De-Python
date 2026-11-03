print("""           ====================
                Lojas 100
           ====================""")
preco = float(input("Digite o valor do produto ou da sua compra:R$"))
forma_de_pagamento = input("""Qual a forma de pagamento?
[1] A vista Dinheiro/Cheque
[2] A vista no Cartão
[3] Em até 2x no cartão
[4] 3x ou mais no cartão
Forma de pagamento:""")
if forma_de_pagamento != "1" and forma_de_pagamento != "2" and forma_de_pagamento != "3" and forma_de_pagamento != "4":
   print("\033[2;31mERRO...\nDigite uma resposta válida!\033[m")
else:
    if forma_de_pagamento == "1":
        desconto = (preco * 10) / 100
        novo_preco = preco - desconto
        print(f"Sua compra de R${preco} paga a vista em dinheiro/cheque tem desconto de 10%!\nEntão sua compra ficou no valor de R${novo_preco:.2f}!")
    elif forma_de_pagamento == "2":
        desconto = (preco * 5) / 100
        novo_preco = preco - desconto
        print(f"Sua compra de R${preco} paga a vista no Cartão tem desconto de 5%!\n Então sua compra ficou no valor de R${novo_preco:.2f}")
    elif forma_de_pagamento == "3":
        print(f"Sua compra de R${preco} foi paga com sucesso em 2x no Cartão!")
    else:
        juros = (preco * 20) / 100
        novo_preco = preco + juros
        print(f"Sua compra de R${preco} paga em 3x ou mais tem uma taxa de juros de 20% então sua compra ficou no valor de R${novo_preco:.2f}")
