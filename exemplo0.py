def exibir_mensagem():
    print("olá")

def calcular_area_triangulo(base, altura):
    area = (base * altura) / 2
    print(f"Área: {area}")
    return area


for i in range(10):
    exibir_mensagem()       #chamar função

base = float(input("Base do triangulo: "))
altura = float(input("Altura do triangulo: "))
area = calcular_area_triangulo(base, altura)       #chamar função
print(f"Área do triangulo: {area}")
