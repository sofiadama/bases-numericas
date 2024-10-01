bits = input('Bits: ')

lista = [int(bit) for bit in bits]

soma = 0
for pos, bit in enumerate(reversed(lista)):
    if bit == 1:
        peso = 2**(pos)
        soma += peso

print(soma)
