media = (float (input('Digite nota 1: ')) + float(input('Digite nota 2: '))) / 2

print('Reprovado' if media < 7 else 'Aprovado com distinção' if media == 10 else 'Aprovado')
