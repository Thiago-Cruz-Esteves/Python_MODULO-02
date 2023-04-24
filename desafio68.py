print('-=-'*20)
print('Sou Computer PRESTOR!!!\nVamos jogar par ou impar!')
print('-=-'*20)
from random import  randint
v=0
while True:
    jo = int(input('Digite o valor: '))
    comp=randint(0,10)
    s = jo + comp
    tipo=' '
    while tipo not in 'PI':
        tipo=str(input('Par ou Impar? [P/I]: ')).strip().upper()[0]
    print(f'Voce jogou {jo} e o Computer PRESTOR  jogou {comp}.\n O total deu {s} que é ')
    if tipo=='P':
        if s %2==0:
            print('Voce venceu')
            v=v+1
        else:
            print('Voce Perdeu!')
            break
    elif tipo=='I':
        if s%2==1:
            print('Voce venceu')
            v=v+1
        else:
            print('Você Perdeu')
            break
    print('Vamos jogar novamente...')
print(f'GAMWE OVER! Você venceu {v} vezes.')




