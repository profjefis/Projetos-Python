# Teste Quiz
import random
perg0='Quanto é 1+1?'
perg1='Quanto é 2+2?'
perg2='Quanto é 3+3?'
perg3='quanto é 4+4?'
resp0='2'
resp1='4'
resp2='6'
resp3='8'
pergs=[perg0,perg1,perg2,perg3]
resps=[resp0,resp1,resp2,resp3]

'''
def pergunta(num):
    varPonto=0
    print(pergs[num])
    if input()==resps[num]:
        print('Certa resposta!')
        varPonto=varPonto+1
    else:
        print('Resposta errada...')
'''
print('Deseja continuar?(digite qualquer tecla para continuar ou tecle "n" para finalizar)')
while input()!='n':
    varPont=0
    for num in range (0,len(pergs)):
        print(pergs[num])
        if input()==resps[num]:
            print('Certa resposta!')
            varPont=varPont+1
        else:
            print('Resposta errada...')

    print('Sua pontuação foi: '+str(varPont))    
    print('Deseja continuar?(digite qualquer tecla para continuar ou tecle "n" para finalizar)')
    
print('Fim do Quiz')


# print(pergs[2])
