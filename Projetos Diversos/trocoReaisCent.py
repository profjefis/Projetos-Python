valorNotasReais = [100,50,20,10,5,2,1,0.5,0.25,0.1,0.05,0.01]

valorNotasReaisFormat = []
for n in range (len(valorNotasReais)):
    valorNotasReaisFormat.append('{:,.2f}'.format(float((valorNotasReais[n] * 100) / 100)))

valorNotasCent = []
for n in range (len(valorNotasReais)):
    valorNotasCent.append(int(valorNotasReais[n] * 100))

valorCompraReais = float(input('Qual o valor da compra: '))
valorCompraCent = valorCompraReais  * 100
valorRecebidoReais = float(input('Qual o valor recebido: '))
valorRecebidoCent = valorRecebidoReais * 100

if valorRecebidoReais > valorCompraReais:
    valorTrocoCent = valorRecebidoCent - valorCompraCent
    valorTrocoReaisFormat = ('{:,.2f}'.format(float(valorTrocoCent / 100)))

    def contNotas(n):
        if n == 0:
            return valorTrocoCent
        else:
            return contNotas(n-1) % valorNotasCent[n-1]

    quantNotas = []
    for n in range (len(valorNotasCent)):
        quantNotas.append(int(contNotas(n) // valorNotasCent[n]))
      
    print('Seu troco é de: R$',valorTrocoReaisFormat)
    print('Este valor pode ser dado em: ')

    for n in range (len(valorNotasCent)):
        if quantNotas[n] != 0:
            if valorNotasReais[n] > 1:
                if quantNotas[n] == 1:
                    print(quantNotas[n],'nota de R$',valorNotasReaisFormat[n])
                else:
                    print(quantNotas[n],'notas de R$',valorNotasReaisFormat[n])        
            else:
                if quantNotas[n] == 1:
                    print(quantNotas[n],'moeda de R$',valorNotasReaisFormat[n])
                else:
                    print(quantNotas[n],'moedas de R$',valorNotasReaisFormat[n]) 
else:
    if valorRecebidoReais == valorCompraReais:
        print('Não há troco!')
    else:
        print('Erro! O valor de compra foi maior que o recebido!') 
