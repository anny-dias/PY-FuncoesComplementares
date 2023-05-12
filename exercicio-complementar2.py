#Dizemos que um número natural é triangular se ele é produto de três números naturais 
#consecutivos. Por exemplo: 120 é triangular, pois 4 * 5 * 6 = 120. 2730 é triangular, 
#pois 13 * 14 * 15 = 2730. Faça uma função que receba um número inteiro e retorne Truese 
#for um número triangular e False, caso contrário.

def triangular(numero):
    if type(numero) != int or numero < 0:
        raise TypeError
    
    for a in range(numero):
        if a * (a+1) * (a+2) == numero:
            return True

    return False

controle = True
while controle:             #solicite vários números ao usuário até que ele digite zero
    while True:             #repete quando houver exceções
        try:
            numero = int(input("Insira um numero inteiro: "))
            if numero == 0:
                controle = False
                print('Programada finalizado')
                break
            if triangular(numero) == True:
                print(f'O numero {numero} é triangular')
            else:
                print(f'O numero {numero} não é triangular')
        except ValueError:
            print('ERRO: o valor inserido não é inteiro')
        except TypeError as erro:
            print('ERRO: {erro}')
        else:
            print('Programada finalizado')
            break
            
    
    