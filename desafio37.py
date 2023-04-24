n=int(input('Digite numero inteiro? '))
print('[1] para BINARIO;\n[2] para OCTAL;\n[3] para HEXADECIMAL.')
op=int(input('Sua opção: '))
b=bin(n)
o=oct(n)
h=hex(n)
if op==1:
    print('{} convertido para BINARIO é igual a {}'.format(n,b[2:]))
elif op==2:
    print('{} convertido para OCTAL é igual a {}'.format(n,o[2:]))
elif op==3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(n,h[2:]))