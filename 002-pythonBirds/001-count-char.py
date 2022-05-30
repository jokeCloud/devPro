#! /usr/bin/python3
'''
    funcao que conta caracteres de uma string
    Ex:
    >>> contar_caracteres('emerson')
    e: 2
    m: 1
    n: 1
    o: 1
    r: 1
    s: 1
    >>> contar_caracteres('ovo')
    o: 2
    v: 1

    :param = string a ser contada
'''

def contar_caracteres(s):
    caracteres_ordenados = sorted(s)
    print(caracteres_ordenados)

    caracter_anterior = caracteres_ordenados[0]
    contagem = 1

    for caracter in caracteres_ordenados[1:]:
        if caracter == caracter_anterior:
            contagem += 1
        else:
            print(f'{caracter_anterior}: {contagem}')
            caracter_anterior = caracter
            contagem = 1

    print(f'{caracter_anterior}: {contagem}')

if __name__ == '__main__':
    contar_caracteres('aannbbaabbnnbbaannaazz')
    contar_caracteres('ovo')

'''
    funcao que conta caracteres de uma string
    Ex:
    >>> contar_caracteres('aannbbaabbnnbbaannaazz')
    {'e': 2, 'm': 1, 'n': 1, 'o': 1, 'r': 1, 's': 1}
    >>> contar_caracteres('ovo')
    {'o': 2, 'v': 1}

    :param = string a ser contada
'''

def transpilar_obj(s):    
    resultado = {}
    for caracter in s:
        resultado[caracter] = resultado.get(caracter, 0) + 1
            
    return resultado

if __name__ == '__main__':
    print(transpilar_obj('aannbbaabbnnbbaannaazz'))
    print(transpilar_obj('ovo'))



