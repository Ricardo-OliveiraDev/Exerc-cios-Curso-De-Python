precos = ("lápis", 1.75,
          "caderno", 20.00,
          "borracha", 3.00,
          "mochila", 120.00,
          "bicicleta", 500.00
          )
for c in range (len(precos)):
    if c % 2 == 0:
        print(f"{precos[c]:.<30}R$",end= "")
    else:
        print(f"{precos[c]:>7.2f}")
