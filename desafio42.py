a=float(input('Digi um numero: '))
b=float(input('Digi um numero: '))
c=float(input('Digi um numero: '))
if a<b+c and b<a+c and c<a+b:
    print('Esses valores forman um triangulo!')
    if a==b==c:
       print('É triangulo equilatero pois tosdos os  lados iguis')
    if a==b or b==c or c==a:
       print('É triangulo  isósceles que tem dois lados iguas')
    if a!=b!=c!=a:
        print('É triangulo escaleno pois nem um dos lado são iguis')


