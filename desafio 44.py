print('='*40)
print('{:^40}'.format('LOJA ESTVES'))
print('='*40)
pr=float(input('Qual valor do produto? '))
print('''Formas de pagamento
[1] a vista dinheiro/cheque.
[2] a vista cartão.
[3] 2x no cartão
[4] 3x ou mais no cartão''')
pg=(int(input('Qual é forma de pagamento? ')))
din=pr-(pr*0.1)
cheq=pr-(pr*0.1)
vist=pr-(pr*0.05)
x2=pr
x3=pr+(pr*0.20)
if 1==pg:
    print('Valor ser pago de R$:{:.2f}'.format(din))
elif 2==pg:
    print('Valor ser pago de R$:{:.2f}'.format(vist))
elif 3==pg:
    print('São 2 parcelas de R$:{:.2f}.\nValor total é de R$:{:.2f}'.format((x2/2),x2))
elif 4==pg:
    print('São 3 parcelas de R$:{:.2f}.\nValor total é de R$:{:.2f}'.format((x3/2),x3))
else:
    er=0
    print('Forma de pagamento invalida. tente novamente!')
    print('Sua compra de R$:{:.2f} vai custa R$:{:.2f} no final.'.format(pr,er))