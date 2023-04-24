no=str(input('Qual seu nome? '))
if no=='Thiago':
    print('Você é BONITÃO!!!')
elif no=='Pedro' or no=='Maria'or no=='Felipe':
    print('Seu nome é Normal')
elif no in 'Jessica Cladia juliana':
    print('Belo nome')
else:
    print('Tenha bom dia {}!'.format(no))