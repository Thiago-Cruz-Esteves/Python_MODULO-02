totp=0
menorp=0
quantm=0
comparativo=0
barato=' '
while True:
    pro=str(input('Nome do produto: ')).strip().upper()
    preço=float(input('Preço: R$'))
    totp=totp+preço
    comparativo=comparativo+1
    if preço>1000:
        quantm=quantm+1
    if comparativo==1:
        menorp=preço
        barato=pro # serve para qulaquer verificação pois so devinir o objeto EX:'barato=pro'
    else:
        if preço<menorp:
            menorp=preço
            barato=pro
    resp=' '
    while resp not in 'NS':
        resp=str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp=='N':# a posição do (if) é de acordo com while que pertence!
        break
print('{:-^40}'.format('FIM DO PROGRAMA...'))#para utilizar espaço ou centrlizar so com (.format('  ')).
print(f'Total de gasto foi de {totp}')
print(f'Temos {quantm} prdutos custando mais de R$:{quantm}')
print(f'O produto mais barato foi o {barato} que custa R$:{menorp}')
