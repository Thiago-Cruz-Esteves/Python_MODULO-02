si=0
med=0
mi=0
nov=''
totm20=0
for ld in range(1,5):
     print('----{}ª PESSOA----'.format(ld))
     n=str(input('Nome:')).strip()
     i=int(input('Idade:'))
     s=str(input('Sexo [M/F]:')).strip()
     si+=i
     med=si/ld
     if ld==1 and s in "Mm":
          mi=i
          nov=n
     if s in 'Mm'and i>mi:
          mi=i
          nov=n
     if s in 'Ff' and i<20:
          totm20+=1

print(' A media de idade do grupo é de {} anos'.format(med))
print('O homem mais velho tem {} anos e se chama {}.'.format(mi,nov))
print('Ao todo são {} mulhers com menos de 20 anos'.format(totm20))