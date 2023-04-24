print('-'*30)
print('Sequencia de Fibonat')
print('-'*30)
n=int(input('Quantos termos você quer mostrar? '))
t=0
t1=1
print('~'*20)
print('{}-{}'.format(t,t1),end='')
cont=3
while cont<=n:
    t2=t+t1
    print('-{}'.format(t2),end='')
    t=t1
    t1=t2
    cont+=1
print('-FIM!!!')
print('~' * 20)


