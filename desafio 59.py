n=float(input('Digite o primeiro valor: '))
n1=float(input('Digite o segundo valor: '))
op=0
while op!=5:
    print('''[1] SOMAR\n[2] MULTIPLICAR\n[3] MAIOR\n[4] NOVOS NUMEROS\n[5] SAIR DO PROGRAMA''')
    op = int(input('Digite o numero da opçao: '))
    if op==1:
        s=n+n1
        print('A soma entre {} e {} é {:.2f}'.format(n,n1,s))
    elif op==2:
        mult=n*n1
        print('A multiplicação entre {} e {} é {:.2f}'.format(n,n1,mult))
    elif op==3:
        if n>n1:
            maior=n
        else:
            maior=n1
        print('O maior numero entre {} e {} é {:.2f}'.format(n,n1,maior))
    elif op==4:
        print('Digite novamente')
        n = float(input('Digite o primeiro valor: '))
        n1 = float(input('Digite o segundo valor: '))
    elif op == 5:
        print('Finalizando...')
    else:
        print('Opção invalida, tente novamente!')
print('FIM PROGRAMA!.\nVolte sempre')
