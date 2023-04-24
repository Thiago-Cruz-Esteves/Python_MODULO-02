totp=0
menorp=0
totm=0
comparativo=0
barato=''
while True:
    pro=str(input('Nome do produto: ')).strip().upper()
    preço=float(input('Preço:R$ '))
    comparativo = comparativo + 1# vai fazer correr pela lista e comparar um por um
    totp = totp + preço
    if preço>1000:
        totm=totm+1
    if comparativo==1 or preço<menorp: # abreviaçao atrvez do or EXP:'if comparativo==1 or preço<menorp:'
        menorp=preço
        barato=pro # serve para qulaquer verificação pois so devinir o objeto EX:'barato=pro'
    resp=' '
    while resp not in 'NS':
        resp=str(input('Quer continuar?[S/N] ')).strip().upper()[0]
    if resp=='N':# a posição do (if) é de acordo com while que pertence!
        break
print('{:-^40}'.format('FIM DO PROGRAMA...'))#para utilizar espaço ou centrlizar so com (.format('  ')).
print(f'Total de gasto foi de {totp}')
print(f'Temos {totm} prdutos custando mais de R$:1000.00')
print(f'O produto mais barato foi o {barato} que custa R$:{menorp}')
