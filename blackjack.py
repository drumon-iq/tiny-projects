baralho_refer = {
        "2_paus":  2, "2_copas":  2, "2_ouros":  2, "2_spada":  2,
        "3_paus":  3, "3_copas":  3, "3_ouros":  3, "3_spada":  3,
        "4_paus":  4, "4_copas":  4, "4_ouros":  4, "4_spada":  4,
        "5_paus":  5, "5_copas":  5, "5_ouros":  5, "5_spada":  5,
        "6_paus":  6, "6_copas":  6, "6_ouros":  6, "6_spada":  6,
        "7_paus":  7, "7_copas":  7, "7_ouros":  7, "7_spada":  7,
        "8_paus":  8, "8_copas":  8, "8_ouros":  8, "8_spada":  8,
        "9_paus":  9, "9_copas":  9, "9_ouros":  9, "9_spada":  9,
        "10_paus":10, "10_copas":10, "10_ouros":10, "10_spada":10,
        "Q_paus": 10, "Q_copas": 10, "Q_ouros": 10, "Q_spada": 10,
        "V_paus": 10, "V_copas": 10, "V_ouros": 10, "V_spada": 10,
        "K_paus": 10, "K_copas": 10, "K_ouros": 10, "K_spada": 10,
        "A_paus": 11, "A_copas": 11, "A_ouros": 11, "A_spada": 11
        }

def main():

    print('############################')
    print('Preparando baralho ...')

    baralho = list()
    for cartas in baralho_refer.keys():
        baralho.append(cartas)

    print(baralho)

def jogar():

    return

def ler_regras():
    cont = 's'
    while cont == 's' or cont == 'S':
        separador(50)
        print('Lorem ipsum dolor sit amet, officia excepteur ex fugiat reprehenderit enim labore')
        print('culpa sint ad nisi Lorem pariatur mollit ex esse exercitation amet. Nisi anim')
        print('excepteur officia. Reprehenderit nostrud nostrud ipsum Lorem est aliquip')
        print('amet voluptate dolor minim nulla est proident. Nostrud officia pariatur ut')
        print('. Sit irure elit esse ea nulla sunt ex occaecat reprehenderit commodo officia')
        print('Lorem duis laboris cupidatat officia voluptate. Culpa proident adipisicing id')
        print('nulla nisi laboris ex in Lorem sunt duis officia eiusmod. Aliqua reprehenderit ')
        print('excepteur duis sunt velit enim. Voluptate laboris sint cupidatat ullamco ut ea')
        print('consectetur et est culpa et culpa duis.')
        cont = input('Reproduzir texto novamente? (s ou n)')
    return

def mao():

    return

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

def separador(novas_linhas = 0):
    for i in range(novas_linhas):
        print('')
    print('============================')

#test()
separador(40)

print('Ola, bem vindo ao BlackJack para terminais')
nome_jog = input('Comece digitando seu nome: ')
resp = input(f'\n{nome_jog}, voce gostaria de ler as regras antes de começar a jogar? (s ou n)')
if resp == 's' or resp == 'S':
    ler_regras()
main()
