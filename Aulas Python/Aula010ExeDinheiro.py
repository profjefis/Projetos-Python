valor = int(input('Qual o valor do dinheiro? '))
quantNotas100 = int(valor/100)
quantNotas50 = int((valor%100)/50)
quantNotas20 = int(((valor%100)%50)/20)
quantNotas10 = int((((valor%100)%50)%20)/10)
quantNotas5 = int(((((valor%100)%50)%20)%10)/5)
quantNotas2 = int((((((valor%100)%50)%20)%10)%5)/2)
quantNotas1 = int(((((((valor%100)%50)%20)%10)%5)%2)/1)
print('você possui:')
print(quantNotas100,'notas de 100 R$')
print(quantNotas50,'notas de 50 R$')
print(quantNotas20,'notas de 20 R$')
print(quantNotas10,'notas de 10 R$')
print(quantNotas5,'notas de 5 R$')
print(quantNotas2,'notas de 2 R$')
print(quantNotas1,'notas de 1 R$')

