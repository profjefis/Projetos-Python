notas = [100,50,20,10,5,2,1]
valor = int(input('Digite o valor: '))
quantNotas = []

def contNotas(n):
    if n == 0:
        return valor
    else:
        return contNotas(n-1) % notas[n-1]

for n in range (len(notas)):
    change = contNotas(n) // notas[n] 
    quantNotas.append(change)
print(quantNotas)

  

