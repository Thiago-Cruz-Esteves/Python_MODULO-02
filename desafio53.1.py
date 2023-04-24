fn=str(input('Digite uma frase ou nome: ')).strip().upper()
pa=fn.split()
jun=''.join(pa)
inv=jun[::-1]
print('O inverso da {} é {}'.format(jun,inv))
if inv==jun:
    print('Temos um palíndromo!')
else:
    print('Nao temos um palindromo')
