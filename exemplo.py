def exibir_mensagem():
    print("olá")

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"Área: {area}")

def par_ou_impar(numero):
    if numero % 2 == 0:
        print("Par")
    else:
        print("Impar")



while True:
    print('1- Exibir uma mensgem ')
    print('2- Verificar se o número é par ou impar ')
    print('3- Calcular a área do triangulo' )
    print('4- Finalizar ')

    opcao = int(input("Escolha uma opção: "))
    if opcao == 1:
        exibir_mensagem()
    elif opcao == 2:
        numero = int(input("Informe um número: "))
        par_ou_impar(numero)
    elif opcao == 3:
        base = float(input("Base do triangulo: "))
        altura = float(input("Altura do triangulo: "))
        calcular_area_triangulo(base, altura)
    elif opcao == 4:
        print("Fim de execução")
        break


