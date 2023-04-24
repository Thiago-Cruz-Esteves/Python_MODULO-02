cont=s=n=0
n=int(input('Digite um numero: '))
while n!=999:
    s=s+n
    cont=cont+1
    n = int(input('Digite mais um numero ou [999] para parar: '))
print('Você digitou {} numeros e a soma ente eles foi {}'.format(cont,s))
