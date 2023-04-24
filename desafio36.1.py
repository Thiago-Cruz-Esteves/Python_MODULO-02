i=int(input('Qual sua idade? '))
sa=float(input('Qual seu salario? '))
vc=float(input('Qual é o valor da casa? '))
tp=float(input('Quero pagar em quantos anos? '))
ilt=(70-i)
pm=ilt*12
vp=(sa*0.3)
pc=vc/pm
print(vp)
if pc<=vp:
    print('Credito aprovado!\nO valor da sua parcela é de R$:{:.2f} em {:.2f} Vezes por mês!'.format(pc,pm))
elif ilt<tp:
    print('Credito Reprovado! pois seu tempo limite é de {} anos'.format(ilt))
elif pc>vp:
    print('Credito Reprovado!\nPois valor da sua parcela é de R$:{:.2f}.'
          '\nE ecede a sua cota de 23% sobre o salario que é de R$:{:.2f} Vezes por mês!'.format(pc,vp))
