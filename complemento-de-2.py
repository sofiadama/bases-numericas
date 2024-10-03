num = int(input('Número: - '))

binario = []
while num > 0:
    binario.append(num % 2)
    num = num // 2

binario.reverse()
binario[-1:0]

comp_de_2 = [1 - bit for bit in binario]
#bits from the original list are flipped

print(f'Complemento de 2:',*comp_de_2) 
