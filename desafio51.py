print('='*30)
print('{:.^20}'.format('10 TERMOS DE UMA PA'))
print('='*30)
pt=int(input('Primeiro termo: '))
r=int(input('Ração: '))
de=pt+(10-1)*r
for n in range(pt,de,r):
    print('{}'.format(n),end='¬>')
print('Acabou!')


