s = str(input('Qual é seu sexo[M/F]? ')).upper().strip()[0]# usar o fatiamento '[]' para pegar a primeira letra
while s!='M' and s!='F':
    s = str(input('Qual é seu sexo? ')).upper().strip()[0]
print('fim')
