num = int(input('Número: - '))

binario = []
while num > 0:
    binario.append(num % 2)
    num = num // 2

binario.reverse()
binario[-1] = 0

binario = [1 - bit for bit in binario]

print(*binario) 
