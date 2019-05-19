valorNotas = [100,50,20,10,5,2,1]
valor = int(input('Qual o valor do dinheiro? '))
quantNotas = [valor//100,(valor%100)//50,((valor%100)%50)//20,(((valor%100)%50)%20)//10,((((valor%100)%50)%20)%10)//5,(((((valor%100)%50)%20)%10)%5)//2,((((((valor%100)%50)%20)%10)%5)%2)//1]
def printnotas():
    for num in range (len(quantNotas)):
        if quantNotas[num] != 0:            
            if quantNotas[num] == 1:
                print(quantNotas[num],'nota de',valorNotas[num],'R$')
            else:
                print(quantNotas[num],'notas de',valorNotas[num],'R$')        
print('você possui:')
printnotas()



