def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def find_closest_prime(num):
    if is_prime(num):
        return num
    lower_prime = num - 1
    while not is_prime(lower_prime):
        lower_prime -= 1
    higher_prime = num + 1
    while not is_prime(higher_prime):
        higher_prime += 1
    if num - lower_prime < higher_prime - num:
        return lower_prime
    else:
        return higher_prime

num = int(input("Digite um número inteiro entre 1 e 1000: "))
closest_prime = find_closest_prime(num)
print(f"O número primo mais próximo de {num} é {closest_prime}.")
