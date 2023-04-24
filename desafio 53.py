fn=str(input('Digite uma frase ou nome: ')).strip().upper()
pa=fn.split()
jun=''.join(pa)
inv=''
for let in range(len(jun)-1,-1,-1):
    inv+=jun[let]
print('O inverso da {} é {}'.format(jun,inv))
if inv==jun:
    print('Temos um palíndromo!')
else:
    print('Nao temos um palindromo')


#print('Você digitou uma frase {}'.format(fn))

