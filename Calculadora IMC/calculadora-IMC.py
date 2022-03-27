#Calculadora IMC
import os
print ('***********************************')
print ('-----------------------------------')
print ('Cálculo do Índice de Massa Corporal')
print ('-----------------------------------')
print ('')
nome = input ('Olá, Qual é o seu nome?\n')
print ('-----------------------------------')
print ('Por favor',nome,'digite sua altura:')
altura = float (input(''))
print ('-----------------------------------')
print ('Por favor',nome,'digite seu Peso: ')
peso = float (input(''))
print ('-----------------------------------')
imc = peso / altura**2
print('')
print(nome,'Seu IMC é: %.2f' % imc)
print('')
print ('***********************************')
print ('===================================')
if imc < 16:
	print(nome,'voçê tem magreza grave')
elif imc < 17:
	print(nome,'voçê tem magreza moderada')
elif imc < 18.5:
	print('voçê tem magreza leve')
elif imc < 25:
	print('Parabens!',nome,'seu peso está Adequado!')
elif imc < 30:
	print('voçê tem Sobrepeso')
elif imc < 35:
	print('voçê tem Obesidade Grau I')
elif imc < 40:
	print('voçê tem Obesidade Grau II (severa)')
else:
	print('voçê tem Obesidade Grau III (mórbida)')
print ('===================================')
print ('***********************************')
os.system("pause")
