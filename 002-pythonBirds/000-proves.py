#! /usr/bin/python3

arr = list(range(0, 30))
name = 'Emerson'
names = ('Emerson', 'Medalha', 'Negrão')
#print(arr)
#print(name[::])

i = 0

while i < len(names):
    print(names[i])
    i += 1

for v in names:
    print(v)

for i, v in enumerate(names):
    print(i, v)

languages = {
    'pt' : 'portugues',
    'en': 'english'  
}

print(languages['pt'])
print('pt' in languages)

languages['es'] = 'spanish'

for k in languages:
    print(k)

for k in languages.keys():
    print(k)

for v in languages.values():
    print(v)

for k, v in languages.items():
    print(k, v)

print(type(languages))

def helloWorld():
    print('Alow world!')

helloWorld()

def sayName(name, lastName, age=31):
    print(f'Hi {name} {lastName}. Age: {age}.')

sayName('Emerson', 'Medalha', 28)
sayName(age=90, name='Emerson', lastName='Negrão')


#*args = tuple
def soma(*args):
    aux = 0
    for value in args:
        aux += value
    return aux

print(soma(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

#**kwargs = dict
def tipo(**kwargs):
    print(kwargs)
    print(type(kwargs))

tipo(name = 'Emerson', lastName = 'Medalha')

args = (2, 8, 32)
kwargs = {'name': 'em', 'pass': 'aaa'}

def f(*args, **kwargs):
    print(args)
    print(kwargs)
    print('f')

f()
f(1, 2, name = 'Emerson', lastName = 'Medalha')
f(args, kwargs)
f(*args)
f(**kwargs)
f(*args, **kwargs)
