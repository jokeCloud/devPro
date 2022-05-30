#! /usr/bin/python3
class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.idade  = idade
        self.nome   = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá meu nome é {self.nome}.'
    
    @staticmethod
    def metodo_estatico():
        return 42
    
    @classmethod
    def nome_e_atributos_de_classes(cls):
        return f'{cls} - olhos {cls.olhos}'
    
class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_do_pai = super().cumprimentar()
        return f'{cumprimentar_do_pai}. Aperto de mão.'

class Mutante(Pessoa):
    olhos = 7


if __name__ == '__main__':
    renzo = Mutante(nome='Renzo')
    luciano = Pessoa(renzo, nome='Luciano')
    print(Pessoa.cumprimentar(luciano))
    print(id(luciano))
    print(luciano.cumprimentar())
    print(luciano.nome)
    print(luciano.idade)
    for filho in luciano.filhos:
        print(filho.nome)
    del luciano.filhos
    luciano.olhos = 1
    del luciano.olhos
    print(renzo.__dict__)
    print(luciano.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(luciano.olhos)
    print(renzo.olhos)
    print(id(Pessoa.olhos), id(luciano.olhos), id(renzo.olhos))
    print(Pessoa.metodo_estatico(), luciano.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classes(), luciano.nome_e_atributos_de_classes())
    pessoa = Pessoa(nome='João')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(luciano, Pessoa))
    print(isinstance(renzo, Pessoa))
    print(isinstance(renzo, Homem))
    print(isinstance(luciano, Homem))
    print(renzo.olhos)
    print(luciano.cumprimentar())
    print(renzo.cumprimentar())
    homem = Homem(nome='Homem')
    print(pessoa.cumprimentar())
    print(homem.cumprimentar())
