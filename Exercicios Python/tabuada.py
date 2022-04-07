digite = 's'
while (digite == 's'):
    num = int (input('digite um numero de um a dez: '))
    cont = 0
    while (cont<=10):
        print(f'{num} x {cont} = {num*cont}')
        cont += 1
    digite = input('deseja fazer outra tabuada? [s/n]')  
else:
    print('Obrigado por usar o programa!')  