nu=int(input('Digite um numero: '))
tot=0
for n in range(1,nu+1):
    if nu%n==0:
        print('\033[4;34m',end=' ')
        tot+=1
    else:
        print('\033[0;35m',end=' ')
    print('{}'.format(n),end=' ')
print('\n\033[mO numero {} foi divisivel {} vezes'.format(nu,tot))
if tot==2:
    print('O {} é um numero primo!'.format(n))
else:
    print('O {} Não é um numero primo!'.format(n))