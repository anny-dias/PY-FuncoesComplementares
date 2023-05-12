#Crie uma função que receba três números como parâmetros, e retorne True se a soma de quaisquer 
#pares de números gera a soma do terceiro número. Caso contrário retorne False.

def soma(num1, num2, num3):
    if num1 + num2 == num3:
        return True
    elif num1 + num3 == num2:
       return True
    elif num2 + num3 == num1:
        return True
    else:
        return False

while True:
    try:
        num1 = float(input("Insira o primeiro número: "))
        num2 = float(input("Insira o segundo número: "))
        num3 = float(input("Insira o terceiro número: "))
        resultado = soma(num1, num2, num3)
        print(resultado)
    except ValueError:
        print('ERRO: Os valores informados não são números')
    else:
        print('Programa finalizado')
        break
        