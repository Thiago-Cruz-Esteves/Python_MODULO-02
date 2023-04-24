s=0
cont=0
for n in range(1,7):
    nun = int(input('Digite o {} valor: '.format(n)))
    if nun%2==0:
        s+=nun
        cont+=1
print("Você informou {} nùmeros e a soma foi {}".format(cont,s))