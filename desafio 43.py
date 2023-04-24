p=float(input('Qual seu peso? '))
h=float(input('Qual altura? '))
imc=p/(h**2)
print(imc)
if imc<18.5:
    print('Você esta abaixo do peso ideal, pois seu IMC é de {:.2f}'.format(imc))
elif 18.5==imc<25:
    print('Você esta com o peso ideal, pois seu IMC é de {:.2f}'.format(imc))
elif 25==imc<30:
    print('Você esta com sobrepeso, pois seu IMC é de {:.2f}'.format(imc))
elif 30==imc<40:
    print('Você esta com obesidade, pois seu IMC é de {:.2f}'.format(imc))
elif imc>40:
    print('Você esta com obesidade mórmida, pois seu IMC é de {:.2f}'.format(imc))
