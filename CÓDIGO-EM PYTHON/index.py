def mmc(n1,n2,n3):
    if n1>n2 and n1>n3 and n2>n3:
        maior = n1
        meio = n2
    elif n1>n3 and n1>n2 and n3>n2:
        maior = n1
        meio = n3
    elif n2>n1 and n2> n3 and n1>n3:
        maior = n2
        meio = n1
    elif n2>n3 and n2>n1 and n3>n1:
        maior = n2
        meio = n3
    elif n3>n2 and n3>n1 and n2>n1:
        maior = n3
        meio = n2
    elif n3>n1 and n3>n2 and n1>n2:
        maior = n3
        meio = n1

    if maior % n1 == 0 and maior % n2 == 0 and maior % n3 == 0:
        mine = maior
    elif n1 == 2 and n2 == 3 and n3 == 4 or n1 == 3 and n2 == 4 and n3 == 2 or n1 == 4 and n2 == 2 and n3 == 3:
        mine = meio*maior
    else:
        mine = n1*n2*n3
    return mine

def cal_media(n1,n2,n3,opcao):
    if opcao == 1:
        media_ari = (n1+n2+n3)/3
        print('Sua média aritmética é por enquanto {}'.format(media_ari))
    elif opcao == 2:
        media_pon = (n1*5+n2*3+n3*2)/3
        print('Sua média pondeerada é por enquanto {}'.format(media_pon))
    elif opcao == 3:
        somadiv = (n1/mmc(n1,n2,n3))+(n2/mmc(n1,n2,n3))+(n3/mmc(n1,n2,n3))
        media_har = (3*mmc(n1,n2,n3))/somadiv
        print('A média harmonica é por enquanto {}'.format(media_har))
    else:
        print('Opção Invalida')
n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
n3 = float(input('Digite sua terceira nota: '))

opcao = int(input('''Escolha um dos modelos abaixo:
[1] Calcular média aritmética
[2] Calcular média ponderada
[3] Calcular média harmonica
Qual opção você escolhera: '''))
cal_media(n1, n2, n3, opcao)
while n1 >= 0 and n2 >= 0 and n3 >= 0:
    n1 = float(input('Digite sua primeira nota: '))
    n2 = float(input('Digite sua segunda nota: '))
    n3 = float(input('Digite sua terceira nota: '))

    opcao = int(input('''Escolha um dos modelos abaixo:
    [1] Calcular média aritmética
    [2] Calcular média ponderada
    [3] Calcular média harmonica
    Qual opção você escolhera: '''))
    cal_media(n1, n2, n3, opcao)