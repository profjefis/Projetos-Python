listFat = []

def fat(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fat(n-1)

valor = int(input('Digite o valor de n: '))
        
for n in range (1,valor + 1):
    listFat.append(fat(n))
print(listFat)

