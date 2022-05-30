#! /usr/bin/python3

'''
#001-Faça um Programa que peça dois números e imprima o maior deles.
n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))

if (n1 > n2):
  print(f'Maior número é: {n1:.2f}')
else:
  print(f'Maior número é: {n2:.2f}')

#002 - Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo
n = float(input('Digite um número: '))

if (n < 0):
  print('Número é negativo!')
else:
  print('Número é positivo')

#003 - Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
letra = input('Digite "F" ou "M", outras letras não serão válidas. ')

if (letra == 'F' or letra == 'f'):
  print(f'Você digitou "{letra}". Sexo feminino. Obrigado!')
elif letra == 'M' or letra == 'm':
  print(f'Você digitou "{letra}". Sexo masculino. Obrigado!')
else:
  print(f'Você não digitou "M" ou "F", digitou "{letra}" engraçadinho(a). Sexo inválido.')

#004 - Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

letra = input('Digite uma letra: ').upper()
vogais = ['A', 'E', 'I', 'O', 'U']

if(letra in vogais):
  print('vogal')
else:
  print('consoante')
  
#005 - Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar:
        A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
        A mensagem "Reprovado", se a média for menor do que sete;
        A mensagem "Aprovado com Distinção", se a média for igual a dez.

n1 = float(input('Digite sua primeira nota: '))
n2 = float(input('Digite sua segunda nota: '))
total_notas = n1 + n2
media = total_notas / 2

if (media == 10):
  print(f'Aprovado com distinção, parabéns!!! \o/ =*')
elif (media >= 7):
  print(f'media: {media:.2f}, você foi aprovado! =)')
else:
  print(f'media: {media:.2f}, você foi reprovado. =(')

#006 - Faça um Programa que leia três números e mostre o maior deles. 

n1 = float(input('Digite um número: '))
n2 = float(input('Outro: '))
n3 = float(input('Mais um: '))

if n1 > n2 and n1 > n3:
  print(f'primeiro número é o maior entre todos')
elif n2 > n1 and n2 > n3:
  print(f'segundo número é o maior entre todos')
elif n3 > n1 and n3 > n2:
  print(f'terceiro número é o maior entre todos')
else:
  print(f'números repetidos: 1º {n1}, 2º {n2}, 3º {n3}, impossível calcular o maior.')


#019 - Faça um Programa que leia um número inteiro menor que 1000 e imprima a quantidade de centenas, dezenas e unidades do mesmo.
        Observando os termos no plural a colocação do "e", da vírgula entre outros. Exemplo:
          326 = 3 centenas, 2 dezenas e 6 unidades
          12 = 1 dezena e 2 unidades Testar com: 326, 300, 100, 320, 310,305, 301, 101, 311, 111, 25, 20, 10, 21, 11, 1, 7 e 16


numero = int(input('Entre com um número inteiro menor que 1000: '))

if numero >= 1000 or numero <= 0:
    print('O número deve ser menor que "1000" e maior que "0".')
    exit()

centenas = numero // 100
resto_centenas = numero % 100
dezenas = resto_centenas // 10
unidades = resto_centenas % 10

if centenas == 1:
    texto_centenas = f'{centenas} centena'
else:
    texto_centenas = f'{centenas} centenas'

if dezenas == 1:
    texto_dezenas = f'{dezenas} dezena'
else:
    texto_dezenas = f'{dezenas} dezenas'

if unidades == 1:
    texto_unidades = f'{unidades} unidade'
else:
    texto_unidades = f'{unidades} unidades'

print(f'{texto_centenas}, {texto_dezenas} e {texto_unidades}.')

#021 - Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

saque = int(input('Qual o valor que deseja sacar? Mín: 10 Máx: 600: '))
if(saque < 10 or saque > 600):
    print('O saque tem de estar dentro dos limites!')
    exit()

notas_100, saque = divmod(saque, 100)
notas_50,  saque = divmod(saque, 50)
notas_10,  saque = divmod(saque, 10)
notas_5, notas_1 = divmod(saque, 5)

print(f'Notas de 100: {notas_100}')
print(f'Notas de 50 : {notas_50}')
print(f'Notas de 10 : {notas_10}')
print(f'Notas de 5  : {notas_5}')
print(f'Notas de 1  : {notas_1}')


'''







