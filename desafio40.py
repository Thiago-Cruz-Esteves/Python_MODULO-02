nt1=float(input('Qual sua primeira nota: '))
nt2=float(input('Qual sua segumda nota: '))
med=(nt1+nt2)/2
if med<5:
    print('REPROVADO, pois sua media foi de {:.2f}'.format(med))
elif med==5 or med<=6.5:
    print('RECUPERAÇÃO, pois sua media foi de {:.2f}'.format(med))
elif med>=7:
    print('APROVADO!, pois sua media foi de {:.2f}'.format(med))
