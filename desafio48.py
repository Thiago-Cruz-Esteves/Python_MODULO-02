s=0
cont=0
for n in range(1,501,2):
    if n%3==0:
     s+=n #cont=cont+1
     cont+=1 #s=s+n
print('A soma de todos os valores é {} e a quantidade é de {} numeros'.format(s,cont))
