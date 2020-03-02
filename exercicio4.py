n1, n2 = float(input('Digite o primeiro numero: ')), float(input('Digite o segundo numero: '))

operacao = input('Escolha a operação ( + , - , / , *): ')

if operacao == '+':
    total = n1 + n2    
elif operacao == '-':
    total = n1 - n2
elif operacao == '*':
    total = n1 * n2
else:
    total = n1 / n2

#Verificar se o TOTAL é decimal:
chegouNoPonto = False
somaDecimais = 0
for i in str(total):
    if not chegouNoPonto:
        if(i == '.'): 
            chegouNoPonto = True
    else:
        somaDecimais += int(i)

if(somaDecimais == 0): total = int(total) 

print('\nTotal:', total)
print('Impar' if total%2 else 'Par')
print('Positivo' if total >= 0 else 'Negativo')
print('Inteiro' if somaDecimais == 0 else 'Decimal')