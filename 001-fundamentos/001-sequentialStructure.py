#! /usr/bin/python3
#001 - Faça um Programa que mostre a mensagem "Alo mundo" na tela.
print('Olá mundo!')


#002 - Faça um Programa que peça um número e então mostre a mensagem O número informado foi [número].
numero = int(input('Digite um número: '))
print(f'o numero digitado foi: {numero}')

#003 - Faça um Programa que peça dois números e imprima a soma.
n1 = int(input('Digite o primeiro número para a soma: '))
n2 = int(input('Digite o segundo número para a soma: '))
print(f'a soma de {n1} + {n2}, é {n1+n2}')

#004 - Faça um Programa que peça as 4 notas bimestrais e mostre a média.
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
n3 = int(input('Digite a terceira nota: '))
n4 = int(input('Digite a quarta nota: '))

print(f'a média das notas é {(n1+n2+n3+n4)/4}')

#005 - Faça um Programa que converta metros para centímetros.
metros = float(input('Digite a quantidade de metros: '))
print(f'{metros:.2f} metros são {metros*100:.2f} centímetros')

#006 - Faça um Programa que peça o raio de um círculo, calcule e mostre sua área.
import math

raio = float(input('Digite o raio do círculo: '))
area = math.pi*raio**2

print(f'A área deste círculo é: {area:.2f}')

#007 - Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.
altura  = float(input('Digite a altura do quadrado: '))
largura = float(input('Digite a largura do quadrado: '))

areaQ = altura * largura
print(f'A área do quadrado é: {areaQ:.2f}, o dobro é {areaQ*2:.2f}')

#008 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valorHora      = float(input('Quanto você recebe por hora? '))
horasTrampadas = int(input('Quantas horas trabalhou nesse mês? '))

print(f'Seu salário nesse mês respectivo a {horasTrampadas} horas trabalhadas e recebe {valorHora:.2f} por hora é dê: {(horasTrampadas*valorHora):.2f}')


#009 - Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).
f = float(input('Digite a temperatura em fahrenheit: '))
c = 5 * ((f-32) / 9)

print(f'{f:.3f} °F é equivalente a {c:.3f} °C')

#010 - Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
c = float(input('Digite a temperatura em celsius: '))
f = c * (9/5) + 32

print(f'{c:.3f} °C é equivalente a {f:.3f} °F')

#011 - Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
nReal1   = float(input('Digite um número inteiro, ex.:(1, -1, 3, 0, -5): '))
nReal2   = float(input('Mais um por favor, ex.:(1, -1, 3, 0, -5): '))
nDecimal = float(input('Digite agora um número real, ex.:(1.2, -0.3, 10.3, -155.4): '))

#o produto do dobro do primeiro com metade do segundo.
calc1 = (2 * nReal1) * (nReal2/2)

#a soma do triplo do primeiro com o terceiro.
calc2 = (3 * nReal1) + nDecimal

#o terceiro elevado ao cubo.
calc3 = nDecimal ** 3

print('')
print(f'dobro do primeiro "x" metade do segundo: {calc1:.2f}')
print(f'triplo do primeiro "+" terceiro: {calc2:.2f}')
print(f'terceiro elevado ao cubo: {calc3:.2f}')

#012 - Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula:
#  (72.7*altura) - 58

altura = float(input('Digite sua altura: '))
pesoIdeal = altura*72.7 - 58
print(f'Seu peso ideal é: {pesoIdeal}')

#013 - Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
#       Para homens: (72.7*h) - 58
#       Para mulheres: (62.1*h) - 44.7
h = float(input('Digite sua altura: '))
pesoIdealHomem = h*72.7 - 58
pesoIdealMulher = h*62.1 - 44.7

print(f'Peso ideal para homem com {h:.2f} de altura é: {pesoIdealHomem:.2f} Kg. O de Mulher é: {pesoIdealMulher:.2f} Kg.')

#014 - João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.

pesoPeixe = float(input('Quantos "Kg" pescou hoje João? '))
limitePermitido = 50
valorMulta = 4
excedente = 0


if (pesoPeixe > limitePermitido):
    excedente = pesoPeixe - limitePermitido

print(f'Peso dos peixes: {pesoPeixe:.2f} Kg, limite permitido nesse estado(SP): {limitePermitido:.2f} Kg. Multa: R$ {(valorMulta * excedente):.2f}.')

'''
015 - Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
salário bruto.
  ° quanto pagou ao INSS.
  ° quanto pagou ao sindicato.
  ° o salário líquido.
  ° calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$
'''
# pensar no design, pois o sistema deve ser dinâmico a alterações dos valores das variáveis
salarioHora = float(input('Quanto você recebe por hora? '))
horasPorMes = int(input('Quantas horas trabalhou nesse mês? '))

salarioBruto = salarioHora * horasPorMes
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
descontos = ir + inss + sindicato
salarioLiquido = salarioBruto - descontos

i = 0.11
s = 0.08
c = 0.05

print(f'Salário bruto(100%): R$ {salarioBruto:.2f}, IR({(100*i):.0f}%): R$ {ir:.2f}, INSS({(100*s):.0f}%): R$ {inss:.2f}, Sindicato({(100*c):.0f}%): R$ {sindicato:.2f}, total de descontos({(100*(i+s+c)):.0f}%): R$ {descontos:.2f}, salário líquido(76%): R$ {salarioLiquido:.2f}')

print(f'Salário bruto(100%): R$ {salarioBruto:.2f}, IR(11%): R$ {ir:.2f}, INSS(8%): R$ {inss:.2f}, Sindicato(5%): R$ {sindicato:.2f}, total de descontos(24%): R$ {descontos:.2f}, salário líquido(76%): R$ {salarioLiquido:.2f}')

#016 - Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.

tamanhoAreaM2 = float(input('Qual o tamanho da área em metros quadrados que vai ser pintada? '))
tinta = 1
proporcao = tinta * 3
litrosLataTinta = tinta * 18
precoLata = 80.00

latasNecessarias = tamanhoAreaM2 / proporcao
totalComprar = latasNecessarias * precoLata

print(f'Para pintar uma área de {tamanhoAreaM2} M3 é necessário {latasNecessarias:.0f} latas de tinta, que ficam no preço de R$ {totalComprar:.2f}. Obrigado, volte sempre!')

'''
#017 - Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
  Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    comprar apenas latas de 18 litros;
    comprar apenas galões de 3,6 litros;
    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
'''
import math

areaM3 = int(input('Qual a área em metros quadrados a ser pintada? '))

folga = areaM3*1.1
litroMetro = 6
lata = 18
latasParaPintar = folga / litroMetro
qtdLata = math.ceil(latasParaPintar / lata)
valorLatas = qtdLata*80
print(f"Será preciso {qtdLata} lata's de 18 litros, no valor de R${valorLatas:.2f}.")

galoesParaPintar = folga / litroMetro
galao = 3.6
qtdGaloes = math.ceil(latasParaPintar / galao)
valorGaloes = qtdGaloes*25
print(f'Será preciso {qtdGaloes} galão(ões) de 3.6 litros, no valor de R${valorGaloes:.2f}.')

qtdLata = math.floor(latasParaPintar / lata)
valorLatas = qtdLata*80
litroFaltante = latasParaPintar % lata
qtdGaloes = math.ceil(litroFaltante / galao)
valorGaloes = qtdGaloes*25
valorTotal = valorLatas + valorGaloes
print(f"Será preciso {qtdLata} lata's de 18 litros mais {qtdGaloes} galão(ões) de 3.6 litros, no valor de R$ {valorTotal:.2f}.")


#018 - Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).

arquivo = float(input('Qual o tamanho do arquivo em megabytes? '))
internet = float(input('Qual a velocidade da sua internet em megabits por segundo? '))

bit = 8
arquivo *= bit
tempoDownload = arquivo / 60

print(f"O arquivo de tamanho {(arquivo/8):.2f} Mb's será baixado em {tempoDownload:.2f} minutos. Obrigado!")
















