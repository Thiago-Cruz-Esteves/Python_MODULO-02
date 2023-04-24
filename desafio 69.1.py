tot18=toth=totm20=0
while True:
    i=int(input('Idade: '))
    s=' '
    while s not in'MF':#n para faza a pergunta novamente se for diferente do que ele quer
        s=str(input('Sexo: [M/F]')).strip().upper()[0]
    if i>18:
        tot18=tot18+1
    if s=='M':
        toth=toth+1
    if s=='F' and i<20:
        totm20=totm20+1
    resp=' '
    while resp not in 'SN':# tudo que esta em (in) tem ser colocado EX: in'Nn'
        resp=str(input('Quer continuar?[S/N]')).strip().upper()[0]
    if resp=='N':# testo dentro da '  ' tem que ser maiusculo porque o .upper esta ativado EX:'N'
        break
print(f'Total de pessoas com mais de 18 anos:{tot18}')
print(f'Ao todo temos {toth} homens cadastrados')
print(f'E temos {totm20} mulheres com menos de 20')