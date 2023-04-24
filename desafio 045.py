from random import randint
from time import sleep
it=('TESORA','PAPEL','PEDRA')
comp=randint( 0, 2)
print('O computador escolheu {}!'.format(it[comp]))
print('-=-'*10)
print('''SUAS OPÇOES:
[0] TESORA
[1] PAPEL
[2] PEDRA''')
print('-=-'*10)
jo=int(input('QUAL É SUA JOGADA? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
if comp==0:
    if jo==0:
        print('EMPATE')
    elif jo == 1:
        print('O COMPUTADOR GANHO')
    elif jo == 2:
        print('VOCÊ GANHO! ')
    else:
        print('Jogada invalida')
elif comp==1:
    if jo==0:
        print('VOCÊ GANHO')
    elif jo == 1:
        print('EMPATE')
    elif jo == 2:
        print('O COMPUTADOR GANHO! ')
    else:
        print('Jogada invalida')
elif comp==2:
    if jo == 0:
        print('O COMPUTADOR GANHO')
    elif jo == 1:
        print('VOCÊ GANHO!')
    elif jo == 2:
        print('EMPATE ')
    else:
        print('Jogada invalida')