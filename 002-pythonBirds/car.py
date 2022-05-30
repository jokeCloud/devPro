#! /usr/bin/python3
"""
Você deve crirar uma clase carro que vai possuir
dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O Motor terá a responsabilidade de controlar a velocidade.
Ele oferece os seguintes atributos:
1) Atributo de dados velocidade
2) Método acelerar, que deverá incrementar a velocidade de uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades
   
A Direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Note, Sul, Leste, Oeste.
2) Métido girar a direta
3) Método girar a esquerda

    N
O       L
    S
    
Exemplo:
    >>> #Testando motor
    >>> motor = Motor()
    >>> motor.velocidade
    0
    >>> motor.acelerar()
    >>> motor.velocidade
    1
    >>> motor = acelerar()
    >>> motor.velocidade
    2
    >>> motor = acelerar()
    >>> motor.velocidade
    3    
    >>> motor = frear()
    >>> motor.velocidade
    1    
    >>> motor = frear()
    >>> motor.velocidade
    0
    >>> motor = frear()
    >>> motor.velocidade
    0
    >>> #Testando direção
    >>> direcao = Direcao()
    >>> direcao.valor
    'Norte'
    >>> direcao.direita()
    >>> direcao.valor
    'Leste'
    >>> direcao.direita()
    >>> direcao.valor
    'Sul'
    >>> direcao.direita()
    >>> direcao.valor
    'Oeste'
    >>> direcao.direita()
    >>> direcao.valor
    'Norte'
    >>> direcao.esquerda()
    >>> direcao.valor
    'Oeste'
    >>> direcao.esquerda()
    >>> direcao.valor
    'Sul'
    >>> direcao.esquerda()
    >>> direcao.valor
    'Leste'
    >>> direcao.esquerda()
    >>> direcao.valor
    'Norte'
    >>> carro = Carro(direcao, motor)
    >>> carro.calcular_velocidade()
    0
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    1
    >>> carro.acelerar()
    >>> carro.calcular_velocidade()
    2
    >>> carro.frear()
    >>> carro.calcular_velocidade()
    0
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.direita()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.direita()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.direita()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.direita()
    >>> carro.calcular_direcao()
    'Norte'
    >>> carro.esquerda()
    >>> carro.calcular_direcao()
    'Oeste'
    >>> carro.esquerda()
    >>> carro.calcular_direcao()
    'Sul'
    >>> carro.esquerda()
    >>> carro.calcular_direcao()
    'Leste'
    >>> carro.esquerda()
    >>> carro.calcular_direcao()
    'Norte'
"""

class Carro:
    def __init__(self, motor, direcao):
        self.motor   = motor
        self.direcao = direcao
        
    def calcular_velocidade(self):
        return self.motor.velocidade
    
    def acelerar(self):
        self.motor.acelerar()
        
    def frear(self):
        self.motor.frear()
        
    def calcular_direcao(self):
        self.direcao.valor
    
    def girar_a_direita(self):
        self.direcao.direita()
    
    def girar_a_esquerda(self):
        self.direcao.esquerda()


class Motor:
    def __init__(self):
        self.velocidade = 0
    
    def acelerar(self):
        self.velocidade += 1
    
    def frear(self):
        self.velocidade -= 2
        self.velocidade = max(0, self.velocidade)

NORTE = 'Norte'
LESTE = 'Leste'
SUL   = 'Sul'
OESTE = 'Oeste'

class Direcao:
    
    rotacao_direita_dct = {
        NORTE: LESTE, LESTE: SUL, SUL: OESTE, OESTE: NORTE
    }
    rotacao_esquerda_dct = {
        NORTE: OESTE, OESTE: SUL, SUL: LESTE, LESTE: NORTE
    }
    
    def __init__(self):
        self.valor = NORTE
        
    def direita(self):
        self.valor = self.rotacao_direita_dct[self.valor]
    
    def esquerda(self):
        self.valor = self.rotacao_esquerda_dct[self.valor]


motor = Motor()
orientacao = Direcao()
carro = Carro(motor, orientacao)
 

'''      
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)

print('')
motor.frear()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)

print('')
print(orientacao.valor)
orientacao.direita()
print(orientacao.valor)
orientacao.direita()
print(orientacao.valor)
orientacao.direita()
print(orientacao.valor)
orientacao.direita()
print(orientacao.valor)

print('')
print(orientacao.valor)
orientacao.esquerda()
print(orientacao.valor)
orientacao.esquerda()
print(orientacao.valor)
orientacao.esquerda()
print(orientacao.valor)
orientacao.esquerda()
print(orientacao.valor)

print('')
print(carro.calcular_direcao())
print(carro.calcular_velocidade())
carro.acelerar()
print(carro.calcular_velocidade())
'''