print('='*30)
print('{:.^20}'.format('10 TERMOS DE UMA PA'))
print('='*30)
pt=int(input('Primeiro termo: '))
r=int(input('Ração: '))
cont=1
termo=pt
total=0
mais=10
while mais !=0:
    total=total+mais
    while cont <= total:
        print('{} --'.format(termo), end='')
        termo = termo + r
        cont = cont + 1
    print('pauda')
    mais = int(input('Quantos temos você quer mostrar a mais? '))
print('FIM...')

