print('Olá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')
                                                                                
nome = input('Qual seu nome? ')                                                             
                                                                                
print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('As opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n') #COR       
                                                                                
input('Aperte ENTER para continuar...')                                                  
                                                                                
print('\nO jogo já vai começar! Lá vem a primeira questão!')
print('\nVamos começar com questões do nível FACIL!')                             
                                                                                
input('Aperte ENTER para continuar...')


print('\n\n' + '-'*40)

ajuda = 2
pulo = 3
resposta = input("Qual a sua reposta?! ")
if resposta == "ajuda":
    ajuda -= 1
if ajuda == 0:
    print("ATENÇÃO: Você não tem mais direito a ajudas!")
if resposta == "pula":
    pulo -= 1
if pulo == 0:
    print("ATENÇÃO: Você não tem mais direito de pulos!")