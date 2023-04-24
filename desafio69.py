tot18=sm=tot20=0
while True:
    print('-'*20)
    print('CADASTRE UMA PESSOA')
    print('-'*20)
    i = int(input('Idade: '))
    s = str(input('Sexo:[M/F] ')).strip().upper()[0]
    if i > 18:
        tot18 = tot18 + 1
    if s == 'M':
        sm = sm + 1
    if s== 'F' and i < 20:
        tot20 = tot20 + 1
    con = str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if con== 'N':
        break
print(f'Total de pessoas com mais de 18 anos, foram de {tot18} pessoas.')
print(f'Ao todo temos {sm} homens cadastrados')
print(f'E temos {tot20} mulheres com menos de 20 anos')
