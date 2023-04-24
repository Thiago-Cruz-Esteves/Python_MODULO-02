print('='*30)
print('Banco TCE')
print('='*30)
sacar=float(input('Qual valor você quer sacar? R$: '))
total=sacar
ced=50#essa seria mairo cedula da maquina
totced=0
while True:
    if total>=ced:
        total=total-ced # vai ver o quanto eu posso retirar referente a essa cedula
        totced=totced+1# vai marca a retirada
    else:# verificaçao de ced
        if totced > 0:
            print(f'Total de {totced} Cédulas de R$:{ced}')
        if ced==50:
            ced=20
        elif ced==20:
            ced=10
        elif ced==10:
            ced=1
        totced=0
        if total==0:
            break
print('='*20)
print('Volte sempre ao BANCO CEV! Tenha um bom dia!')

