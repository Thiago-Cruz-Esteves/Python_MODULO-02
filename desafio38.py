n=int(input('Digite um numero: '))
n1=int(input('Digite um numero: '))
if n>n1:
    print("O primeiro valor é maior".format(n))
elif n1>n:
    print("O Segundo valor é maior".format(n1))
else:
    n=n1
    print('Os doi valores são iguis')
