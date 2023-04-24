while True:
    n = int(input('Quer ver tbuada de qual valor? '))
    if n < 0:
        break
    for q in range(1,11):
        print(f'{n}x{q}={n*q}')
print('FIM')