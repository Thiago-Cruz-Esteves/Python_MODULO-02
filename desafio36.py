sa=float(input('Qual seu salario? '))
vc=float(input('Qual é o valor da casa? '))
tp=float(input('Quer pagar em quantos anos? '))
pm=tp*12
vp=sa*0.3
pc=vc/pm
if vp>=pc:
    print('CREDITO APROVADO!\nO valor da sua parcela é de R$:{:.2f} em {:.2f} Vezes por mês!'.format(pc,pm))
elif vp<pc:
    print('CREDITO REPROVADO!\nPois valor da sua parcela é de R$:{:.2f}.'
          '\nE ecede a sua cota de 23% sobre o salario que é de R$:{:.2f} Vezes por mês!'.format(pc,vp))



