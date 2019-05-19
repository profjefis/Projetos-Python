# Teste Quiz
pergunta1='Quanto é 1+1?'
resposta1='2'
pergunta2='Quanto 2+2?'
resposta2='4'

print('Deseja continuar?(digite qualquer tecla para continuar ou tecle "n" para finalizar)')
while input()!='n':
    varPonto=0
    print(pergunta1)
    if input()==resposta1:
        print('Certa resposta!')
        varPonto=varPonto+1
    else:
        print('Resposta errada...')

    print(pergunta2)
    if input()==resposta2:
        print('Certa resposta!')
        varPonto=varPonto+1
    else:
        print('Resposta errada...')

    print('Você fez '+str(varPonto)+' pontos') 
    print('Deseja continuar?(digite qualquer tecla para continuar ou tecle "n" para finalizar)')
print('Fim do Quiz')
