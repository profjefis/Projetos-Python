valorNotas = [100,50,20,10,5,2,1,0.50,0.25,0.10,0.05,0.01]
quantNotas = []

valor = float(input('Qual o valor do dinheiro? '))

def contNotas(n):
    if n == 0:
        return valor
    else:
        return contNotas(n-1) % valorNotas[n-1]

for n in range (len(valorNotas)):
    quantNotas.append(int(contNotas(n) // valorNotas[n]))

print('você possui: ')

for n in range (len(valorNotas)):
    if quantNotas[n] != 0:
        if valorNotas[n] > 1:
            if quantNotas[n] == 1:
                print(quantNotas[n],'nota de',valorNotas[n],'R$')
            else:
                print(quantNotas[n],'notas de',valorNotas[n],'R$')        
        else:
            if quantNotas[n] == 1:
                print(quantNotas[n],'moeda de',valorNotas[n],'R$')
            else:
                print(quantNotas[n],'moedas de',valorNotas[n],'R$') 



