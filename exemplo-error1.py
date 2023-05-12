while True:
    print('1- Soma')
    print('2- Subtração')
    print('3- Multiplicação')
    print('4- Divisão')
    print('5- Sair')
    try:
        opcao = int(input('Escolha uma opção: '))
        
        if opcao == 5:
            print('Fim do programa')
            break
        
        try:
            if opcao >= 1 and opcao <= 4:
                a = float(input('Informe o primeiro número: '))
                b = float(input('Informe o segundo número: '))
        except ValueError:
            print('ERRO: os valores informados não são números')
        else:
            if opcao == 1:
                print(f'Soma {a + b}')
            elif opcao == 2:
                print(f'Subtração {a - b}')
            elif opcao == 3:
                print(f'Multiplicação {a * b}')
            elif opcao == 4:
                try:
                    print(f'Divisão {a / b}')
                except ZeroDivisionError:
                    print('ERRO: Ocorreu uma divisão por zero')
            else:
                print('Opção Inválida')

    except ValueError:
        print('ERRO: Digite um valor entre 1 e 5')
    except Exception:
        print('ERRO: Um erro inesperado')
   