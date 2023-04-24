resp='s'
s=quant=med=maior=menor=0
while resp in'Ss':
    n = float(input('Digite o numero:'))
    s=s+n
    quant = quant + 1
    if quant==1:
        maior=menor=n
    else:
        if n>maior:
            maior=n
        if n<menor:
            menor=n
    resp= str(input('Quer continuar? [S/N]:  ')).strip().upper()[0]
med=s/quant
print('Você digitou {} numeros e a media {}foi'.format(quant,med))
print('O maior foi {} e o menor foi {}'.format(maior,menor))