num = int(input('Número: '))

lista_bits = []

while num > 0:
    resto = num % 2
    lista_bits.append(resto)
    num = num // 2
# '//' arredonda para o inteiro mais proximo

lista_bits.reverse()

print(*lista_bits)  
