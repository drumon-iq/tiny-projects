import random

####################################################################

baralho_refer = {
    #           pontos naipe nome
        "2_paus": [ 2, 'p',   2], "2_copas": [ 2, 'c',   2], "2_ouros": [ 2, 'o',   2], "2_spada": [ 2, 's',   2],
        "3_paus": [ 3, 'p',   3], "3_copas": [ 3, 'c',   3], "3_ouros": [ 3, 'o',   3], "3_spada": [ 3, 's',   3],
        "4_paus": [ 4, 'p',   4], "4_copas": [ 4, 'c',   4], "4_ouros": [ 4, 'o',   4], "4_spada": [ 4, 's',   4],
        "5_paus": [ 5, 'p',   5], "5_copas": [ 5, 'c',   5], "5_ouros": [ 5, 'o',   5], "5_spada": [ 5, 's',   5],
        "6_paus": [ 6, 'p',   6], "6_copas": [ 6, 'c',   6], "6_ouros": [ 6, 'o',   6], "6_spada": [ 6, 's',   6],
        "7_paus": [ 7, 'p',   7], "7_copas": [ 7, 'c',   7], "7_ouros": [ 7, 'o',   7], "7_spada": [ 7, 's',   7],
        "8_paus": [ 8, 'p',   8], "8_copas": [ 8, 'c',   8], "8_ouros": [ 8, 'o',   8], "8_spada": [ 8, 's',   8],
        "9_paus": [ 9, 'p',   9], "9_copas": [ 9, 'c',   9], "9_ouros": [ 9, 'o',   9], "9_spada": [ 9, 's',   9],
        "10_paus":[10, 'p',  10], "10_copas":[10, 'c',  10], "10_ouros":[10, 'o',  10], "10_spada":[10, 's',  10],
        "Q_paus": [10, 'p', "q"], "Q_copas": [10, 'c', "q"], "Q_ouros": [10, 'o', "q"], "Q_spada": [10, 's', "q"],
        "V_paus": [10, 'p', "v"], "V_copas": [10, 'c', "v"], "V_ouros": [10, 'o', "v"], "V_spada": [10, 's', "v"],
        "K_paus": [10, 'p', "k"], "K_copas": [10, 'c', "k"], "K_ouros": [10, 'o', "k"], "K_spada": [10, 's', "k"],
        "A_paus": [11, 'p', "a"], "A_copas": [11, 'c', "a"], "A_ouros": [11, 'o', "a"], "A_spada": [11, 's', "a"]
        }

def main():

    #Embelezamento de terminal
    separador(50,'Novo Jogo')
    print('Preparando baralho ...')

    #Prepara as listas e variaveis do jogo
    baralho = list()
    dealer = list()
    jogador = list()

    #Transforma o dicionario em uma lista
    for cartas in baralho_refer.keys():
        baralho.append(cartas)
    print('Baralho montado')

    distribuir_carta(2, baralho, jogador)
    print('2 cartas distribuidas para o jogador!')

    continuar = True

    if mao_pontos(jogador) == 21:
        separador(3, 'BLACKJACK!')
        print('O jogador tem um BLACKJACK, maravilha!')
        print('Por causa do BLACKJACK sua vez será \"Pulada\"')
        continuar = False

    #Vez do jogador

    while continuar is True:
        separador(3,'Turno do jogador')
        mao_mostrar(jogador)
        if mao_pontos(jogador) >= 21:
                print('Sua mão é igual ou maior a 21 e não é mais possível continuar, vez terminada')
                continuar = False
        else:
            if input('Pegar mais uma carta? (s ou n)') == 's':
                    distribuir_carta(1, baralho, jogador)
            else:
                    continuar = False

    #Debug
#    distribuir_carta(2, baralho, jogador)
#    distribuir_carta(2, baralho, dealer)
#    
#    print(f'Baralho Restante: {baralho}')
#    print(f'Dealer: {dealer}')
#    print(f'Jogador: {jogador}')
#
#    distribuir_carta(2, baralho, jogador)
#
#    print(f'Jogador: {jogador}')
#
#    mostrar_mao(jogador)

def mao_pontos(mao = list()):
    value = list()
    total = 0
    for i in mao:
        total += baralho_refer[i][0]
        value.append(baralho_refer[i][0])

    #Has to check if value has blown the 21 but has an ace, in which remove trying to achieve 21
    while total > 21:
        if value.count(11) == 0: #Could be smarter but I dont know how to error handle
            break
        value.remove(11)
        total -= 10


    return total

def mao_mostrar(mao = list()):
    for i in mao:
        desenhar_carta(i)

def desenhar_carta(card = str()):
    if baralho_refer[card][1] == 's':
        print(f' _____ ')
        print(f'|{baralho_refer[card][2]} .  |')
        print(f'| /.\ |')
        print(f'|(_._)|')
        print(f'|  |  |')
        print(f'|____{baralho_refer[card][2]}|')
    elif baralho_refer[card][1] == 'o':
        print(f' _____ ')
        print(f'|{baralho_refer[card][2]} ^  |')
        print(f'| / \ |')
        print(f'| \ / |')
        print(f'|  .  |')
        print(f'|____{baralho_refer[card][2]}|')
    elif baralho_refer[card][1] == 'p':
        print(f' _____ ')
        print(f'|{baralho_refer[card][2]} _  |')
        print(f'| ( ) |')
        print(f'|(_\'_)|')
        print(f'|  |  |')
        print(f'|____{baralho_refer[card][2]}|')
    elif baralho_refer[card][1] == 'c':
        print(f' _____ ')
        print(f'|{baralho_refer[card][2]}_ _ |')
        print(f'|( v )|')
        print(f'| \ / |')
        print(f'|  .  |')
        print(f'|____{baralho_refer[card][2]}|')

def ler_regras():
    cont = 's'
    while cont == 's' or cont == 'S':
        separador(50,'Regras - Pag 1')
        print('Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore')
        print('culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim')
        print('excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip')
        print('amet voluptate dolor minim nulla est proident. Nostrud officia pariatur ut')
        print('. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia')
        print('Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id')
        print('nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit ')
        print('excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea')
        print('consectetur et est culpa et culpa duis.')
        separador()
        cont = input('Reproduzir texto novamente? (s ou n): ')
    return

def distribuir_carta(qntd = 1, baralho = list(), mao = list()):

    for i in range(qntd):
        carta_nmr = random.randint(0, len(baralho)-1)
        mao.append(baralho.pop(carta_nmr))

def test():
    print('############################')
    print('Test Function:')
    print('Printing base dictionary:')
    print(baralho_refer.keys())
    print('============================')
    print('Card list:')
    i = 0
    for cartas, value in baralho_refer.items():
        print(cartas)
        i += 1
    print('============================')
    print('Total cards: ', i)
    print('============================')

    baral = [cards for cards, value in baralho_refer.items()]
    print(baral)

def separador(novas_linhas = 0, msg = str()):       #Pode ou não receber uma quantidade de linhas para mostrar e uma mensagem 
    for i in range(novas_linhas):                   #Mensagem é definida como vazia com str()
        print('')
    if len(msg) == 0:
        print('·==============================================·\n')
    else:
        print(f'·===<>=========<>===<{msg}>===<>=========<>===·\n')

#test()
separador(40, 'Blackest of the Jackest')

print('Ola, bem vindo ao BlackJack para terminais')
nome_jog = input('Comece digitando seu nome: ')
resp = input(f'\n{nome_jog}, voce gostaria de ler as regras antes de começar a jogar? (s ou n): ')
if resp == 's' or resp == 'S':
    ler_regras()
main()
