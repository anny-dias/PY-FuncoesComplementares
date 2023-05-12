# função para somar dois números INTEIROS

def soma (a,b):
    if type(a) == int and type(b) == int:
        c = a + b
        print(f'Resultado da Soma: {c}')
    else:
        raise TypeError('Os tipos dos parâmetros devem ser inteiros.')
    
a = 2
b = 3.5


try:
    soma(a, b)
except TypeError as msg:
    print(f'ERRO: {msg}')


# função para somar doi números INTEIROS E POSITIVOS

def soma (a,b):
    if type(a) == int and type(b) == int and a > 0 and b > 0:
        c = a + b
        print(f'Resultado da Soma: {c}')
    else:
        raise TypeError('Os tipos dos parâmetros devem ser positivos.')
    
while True:
    try:
        a = int(input("Informe o primeiro número: "))
        b= int(input("Informe o segundo número: "))
    
        if a == 0 and b == 0:           #validando se o número é positivo
            break
        try:
            soma(a, b)
        except TypeError as msg:
            print(f'ERRO: {msg}')

    except ValueError:                  #validando se o número é inteiro (int)
        print('ERRO: os parâmetros devem ser inteiros.')


