def show_regras():
    print("Womp Womp")

print("JOGO DE BLACKJACK")
print("=================")
nome_jog = input("Digite seu nome para começar o jogo: ")
print("Maravilha", nome_jog, "voce ja é familiarizado com as regras ou gostaria de um manual?")

aux = input("S - Ja conheço as regras\nN - Não, gostaria de ler as regras\n")

if aux == "N":
    show_regras()
else:
    print("Okay, prosseguindo para o jogo ...")

