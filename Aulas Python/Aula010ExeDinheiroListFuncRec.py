valorNotas = [100,50,20,10,5,2,1]
quantNotas = []

valor = int(input('Qual o valor do dinheiro? '))

def contNotas(n):
    if n == 0:
        return valor
    else:
        return contNotas(n-1) % valorNotas[n-1]

for n in range (len(valorNotas)):
    quantNotas.append(contNotas(n) // valorNotas[n])

print('você possui: ')

for n in range (len(valorNotas)):
    if quantNotas[n] != 0:            
        if quantNotas[n] == 1:
            print(quantNotas[n],'nota de',valorNotas[n],'R$')
        else:
            print(quantNotas[n],'notas de',valorNotas[n],'R$')        




