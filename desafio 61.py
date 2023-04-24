print('='*30)
print('{:.^20}'.format('10 TERMOS DE UMA PA'))
print('='*30)
pt=int(input('Primeiro termo: '))
r=int(input('Ração: '))
cont=1
termo=pt
while cont<=10:
    print('{} --'.format(termo),end='')
    termo=termo+r
    cont=cont+1
print('fim')

