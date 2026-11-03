ano = int(input("Em que ano você nasceu? Digite para sabermos em qual categoria você irá competir: "))
idade = 2026 - ano
if idade <= 9:
    print(f"Por ter {idade} anos você vai competir na categoria \033[4;34mMIRIM\033[m!")
elif idade <= 14:
    print(f"Por ter {idade} anos de idade você vai competir na categoria \033[4;32mINFANTIL\033[m!")
elif idade <= 19:
    print(f"Por ter {idade} anos de idade você vai competir na categoria \033[4;35mJUNIOR\033[m!")
elif idade <= 25:
    print(f"Por ter {idade} anos de idade você vai competir na categoria \033[4;36mSÊNIOR\033[m! ")
else:
    print(f"Por ter {idade} anos de idade você vai competir na categoria \033[4;31mMASTER\033[m!")
