from datetime import date
at=date.today().year
an=int(input('Qual é o ano do seu nascimento? '))
i=at-an
print('Você tem {} anos.'.format(i))
if i<=9:
    print("E a sua categoria é a MIRIM!")
elif i<=14:
    print("E a sua categoria é a INFANTIL!")
elif i<=19:
    print("E a sua categoria é a JUNIOR!")
elif i<=25:
    print("E a sua categoria é a SÊNIOR!")
elif i>25:
    print("E a sua categoria é a MARTER!")

