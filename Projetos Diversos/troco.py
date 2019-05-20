valorNotas = [10000,5000,2000,1000,500,200,100,50,25,10,5,1]
quantNotas = []

valorCompra = float(input('Qual o valor da compra: ')) * 100
valorRebido = float(input('Qual o valor recebido: ')) * 100
valorTroco = valorRebido - valorCompra

print(valorTroco/100)

def contNotas(n):
    if n == 0:
        return valorTroco
    else:
        return contNotas(n-1) % valorNotas[n-1]

for n in range (len(valorNotas)):
    quantNotas.append(int(contNotas(n) // valorNotas[n]))
print(quantNotas)

print('Seu troco é de:',valorTroco/100,'R$')
print('Este valor pode ser dado em: ')

for n in range (len(valorNotas)):
    if quantNotas[n] != 0:
        if valorNotas[n]/100 > 1:
            if quantNotas[n] == 1:
                print(quantNotas[n],'nota de',valorNotas[n]/100,'R$')
            else:
                print(quantNotas[n],'notas de',valorNotas[n]/100,'R$')        
        else:
            if quantNotas[n] == 1:
                print(quantNotas[n],'moeda de',valorNotas[n]/100,'R$')
            else:
                print(quantNotas[n],'moedas de',valorNotas[n]/100,'R$') 
      
