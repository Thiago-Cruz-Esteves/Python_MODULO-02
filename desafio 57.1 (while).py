s = str(input('Qual é seu sexo[M/F]? ')).upper().strip()[0]# usar o fatiamento '[]' para pegar a primeira letra
while s not in 'MmFf':
    s = str(input('Qual é seu sexo? ')).upper().strip()[0]
print('Sexo {} .Registrado com sucesso!'.format(s))