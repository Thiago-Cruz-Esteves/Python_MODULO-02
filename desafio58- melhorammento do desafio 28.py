print('-=-'*20)
print('Sou Computer PRESTOR!!!'
      '\nPara me vencer deve adivinhar o numero que estou pençando!'
      '\nTente adivinhar um numero entre 0 a 10')
print('-=-'*20)
from random import randint
from time import sleep
comp= randint(0,10)
jo=int(input('Para ter uma chance de vencer o Computer PRESTOR.\n Digite um numero entre 0 a 10: '))
print('PROCESSANDO...')
sleep(1)
tot=1
while not comp==jo:
      tot=tot+1
      print('O Computer PRESTOR peçou em {}'.format(comp))
      jo=int(input('Para ter uma uma nova chance de vencer o Computer PRESTOR.\n Digite um numero entre 0 a 10: '))
print('Você derotou Computer PRESTOR, mas venceu com {} tentativas'.format(tot))