from funcoes import *
from questoes import *

print('\033[35mOlá! Você está na Fortuna DesSoft e terá a oportunidade de enriquecer!\n')
                                                                                
nome = input('\033[mQual seu nome? ')                                                             
                                                                                
print(f'\nOk {nome}, você tem direito a pular 3 vezes e 2 ajudas!')
print('\033[36mAs opções de resposta são "A", "B", "C", "D", "ajuda", "pula" e "parar"!\n') #COR       
                                                                                
input('\033[mAperte ENTER para continuar...')                                                  
                                                                                
print('\nO jogo já vai começar! Lá vem a primeira questão!')
print('\nVamos começar com questões do nível FACIL!')                             
                                                                                
input('Aperte ENTER para continuar...')

print(funcao_geral(lista_questoes))


