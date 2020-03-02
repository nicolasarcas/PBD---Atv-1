tipo, qtd = int(input('1 - File Duplo\n2 - Alcatra\n3 - Picanha\n')),float(input('Qual a quantidade em kg?\n'))
pagamento = int(input('Pagamento:\n1 - Cartão Tabajara\n2 - Outro\n'))

if tipo == 1:
    if qtd > 5:
        total = qtd * 5.80
    else:
        total = qtd * 4.90
    print(f'File Duplo\nQtd:{qtd}\nTotal:{total}')
elif tipo == 2:
    if qtd > 5:
        total = qtd * 6.80
    else:
        total = qtd * 5.90
    print(f'Alcatra\nQtd:{qtd}\nTotal:{total}')
else:
    if qtd > 5:
        total = qtd * 7.80
    else:
        total = qtd * 6.90
    print(f'Picanha\nQtd:{qtd}\nTotal:{total}')

if pagamento == 1:
    desconto = total * 0.05
    print(f'Pagamento: Cartão Tabajara\nDesconto{desconto}')
else:
    desconto = 0
    print(f'Pagamento: Outro\nDesconto: {desconto}')

pagar = total - desconto
print(f'A pagar: {pagar}')
