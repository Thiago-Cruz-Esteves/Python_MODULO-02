from datetime import date
no=str(input('Qual seu nome? '))
an=int(input('Em que ano você nasceu? '))
anot=date.today().year
i=anot-an
v=18-i
p = i - 18
afu=v+anot
if i<18:
    print('{} naceu em {} e tem {} anos em {}!'
          '\n{} so vai se alistar daqui a {} anos em {}.'.format(no,an,i,anot,no,v,afu))
elif i==18:
    print("O {} voce tem se alistar emeditamente!".format(no))
elif i>18:
    print('{} naceu em {} e tem {} anos em {}!'
          '\n{} voce ja passou {} anos do tempo de alistamento!'
          '\nE deveria ter se alistado em {}.'.format(no, an, i, anot, no, p, afu))


