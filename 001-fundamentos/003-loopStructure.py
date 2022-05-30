'''
#001-Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

numero = 0

try:
  numero = int(input('Digite um número entre 1 e 10: '))
except ValueError:
   print(f'"{numero}" não é uma entrada válida, digite um número inteiro.')

while numero > 10 or numero < 1:
  numero = int(input('Digite um número entre 1 e 10: '))

print('Conseguiu, bro!')

#004-Supondo que a população de um país A seja da ordem de 80000 habitantes com uma taxa anual de crescimento de 3% e que a população de B seja     200000 habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos necessários para que a população do país A ultrapasse ou iguale a população do país B, mantidas as taxas de crescimento.

populacaoA = 80_000
taxa_crescimento_a = 1.03

populacaoB = 200_000
taxa_crescimento_b = 1.015

ano = 0

while populacaoA < populacaoB:
  ano += 1
  populacaoA *= taxa_crescimento_a
  populacaoB *= taxa_crescimento_b

  print(f'Ano: {ano}. População do país A: {populacaoA:.0f}, país B: {populacaoB:.0f}')

#007 - Faça um programa que leia 5 números e informe o maior número.

numeros = []
try:
  for numero in range(0, 5):
    numeros.append(int(input(f'Entre com o {numero+1}o. número: ')))
except ValueError:
  print('Digite números válidos: ')

print(max(numeros))

'''


#008 - Faça um programa que leia 5 números e informe a soma e a média dos números.
numeros = []

try:
  for numero in range(0, 5):
    numeros.append(int(input(f'Entre com o {numero+1}o. número: ')))
except ValueError:
  print('Digite números válidos: ')

print(f'maior: {max(numeros)}, total: {sum(numeros)}, media: {sum(numeros)/5}')
