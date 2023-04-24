from datetime import date
ant=date.today().year
totn=0
totm=0
for p in range(1,8):# Reoparar na orde dos elementos ou formulas
    an=int(input('Em que ano a {}ª pessoa nasceu? '.format(p)))
    i = ant - an
    if i>18:
       totm+=1
    else:
        totn+=1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totm))
print('Ao todo tivemos {} pessoas menores de idade'.format(totn))
