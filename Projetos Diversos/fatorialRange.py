#Calcula o fatorial de um número inteiro

print('Digite um numero inteiro')
n=int(input())
fat=1
for num in range(1,n+1):
    fat = fat * num
print(fat)


