from questoes import *
import random
def transforma_base(lista_questoes):
    dicionario = {}
    for pergunta in lista_questoes:
        if pergunta["nivel"] in dicionario:
            dicionario[pergunta["nivel"]].append(pergunta)
        else:
            dicionario[pergunta["nivel"]]=[pergunta]
    return dicionario


    
def valida_questao(dicio_principal):
    dicio2 = {}
    if 'titulo' not in dicio_principal:
        dicio2['titulo']= 'nao_encontrado'
    if 'nivel' not in dicio_principal:
        dicio2['nivel']= 'nao_encontrado'
    if 'opcoes' not in dicio_principal:
        dicio2['opcoes']= 'nao_encontrado'
    if 'correta' not in dicio_principal:
        dicio2['correta']= 'nao_encontrado'
    tamanho_dicio = len(dicio_principal)
    if tamanho_dicio != 4:
        dicio2['outro']= 'numero_chaves_invalido'
    for chave, valor in dicio_principal.items():
        if chave == 'titulo':
            espaco = valor.isspace()
            if espaco == True:
                dicio2['titulo'] = 'vazio'
            elif chave != 'titulo':
                dicio2[valor]= 'nao_encontrado'
        if chave == 'nivel':
            espaco1 = valor.isspace()
            if valor != 'facil' and valor != 'medio' and valor != 'dificil':
                dicio2['nivel']='valor_errado'
            elif espaco1 == True:
                dicio2['nivel'] = 'vazio'
        if chave == 'opcoes':
            soma = 0
            for letras, respostas in valor.items():
                soma += len(letras)
            if soma != 4:
                dicio2['opcoes']='tamanho_invalido'
            else:
                dicio3 = {}
                for letras, respostas in valor.items():
                    espaco2 = respostas.isspace()
                    if letras != 'A' and letras != 'B' and letras != 'C' and letras != 'D':
                        dicio2['opcoes']='chave_invalida_ou_nao_encontrada'
                    elif espaco2 == True:
                        dicio3[letras]= 'vazia'
                        dicio2['opcoes'] = dicio3
                    elif respostas == '':
                        dicio3[letras]= 'vazia'
                        dicio2['opcoes'] = dicio3
                    elif respostas == 'vazia':
                        dicio3[letras] = respostas
                        dicio2['opcoes'] = dicio3
        if chave == 'correta':
            if valor != 'A' and valor != 'B' and valor != 'C' and valor != 'D':
                dicio2['correta'] = 'valor_errado'
    if dicio_principal != dicio2:
        return dicio2
    else:
        return {}

def valida_questoes(lista_questoes):
    lista = []
    for i in range(0, len(lista_questoes)):
        dicio = lista_questoes[i]
        valida = valida_questao(dicio)
        lista.append(valida)
    return lista


def sorteia_questao(dicionario_questoes,nivel):
  questao_sorteada = random.choice(dicionario_questoes[nivel])
  return questao_sorteada


def sorteia_questao(dicionario_questoes,nivel):
    questao_sorteada = random.choice(dicionario_questoes[nivel])
    return questao_sorteada

def sorteia_questao_inedita(dicio_questoes, nivel, lista_sorteada):
  inedita = True
  while inedita == True:
    questao_inedita = sorteia_questao(dicio_questoes,nivel)
    if questao_inedita not in lista_sorteada:
      lista_sorteada.append(questao_inedita)
      inedita = False
    else:
      inedita = True
  return questao_inedita


def questao_para_texto(dicio_questao, num_questao):
    titulo = dicio_questao['titulo']
    nivel = dicio_questao['nivel']
    opcaoA = dicio_questao['opcoes']['A']
    opcaoB = dicio_questao['opcoes']['B']
    opcaoC = dicio_questao['opcoes']['C']
    opcaoD = dicio_questao['opcoes']['D']
    correta = dicio_questao['correta']
    string = '-'*40 + f'\nQUESTAO {num_questao}' + '\n\n' + titulo + '\n\n' + 'RESPOSTAS:' + '\nA: ' + opcaoA + '\nB: ' + opcaoB + '\nC: ' + opcaoC + '\nD: ' + opcaoD
    return string
   
def funcao_ajuda_pulo():
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

def gera_ajuda(dicio_questao):
    correta = dicio_questao['correta']
    opcoes = dicio_questao['opcoes']
    incorretas1 = ''
    if correta == 'A':
        incorretas1 = 'B', 'C', 'D'
    if correta == 'B':
        incorretas1 = 'A', 'C', 'D'
    if correta == 'C':
        incorretas1 = 'A', 'B', 'D'
    if correta == 'D':
        incorretas1 = 'A', 'B', 'C'
    incorretas = list(incorretas1)
    num_aleatorio = random.randint(1,2)
    letra_aleatoria = random.choice(incorretas)
    incorretas.remove(letra_aleatoria) #removendo caractere ja sorteado para usar na dica dupla
    letra_aleatoria2 = random.choice(incorretas)
    alternativa1 = opcoes[letra_aleatoria]
    alternativa2 = opcoes[letra_aleatoria2]
    if num_aleatorio == 1:
        return f"DICA:\nOpções certamente erradas: {alternativa1}"
    else:
        return f"DICA:\nOpções certamente erradas: {alternativa1} | {alternativa2}"


def funcao_geral(lista):
    dicio_base_questoes = transforma_base(lista_questoes)
    niveis = ['facil', 'medio', 'dificil']
    for nivel in niveis:
        for lista1 in dicio_base_questoes[nivel]:
            lista_validada = (valida_questoes(lista1))
        for i in range(0, len(lista_validada)):
            tamanho = len(lista_validada[i])
            if tamanho == 0:
                x = True
            else:
                x = False
            if x == True:
                questao = sorteia_questao_inedita(dicio_base_questoes, nivel)
                for i in range(0, 10):
                    num_questao = i
                    quest = questao_para_texto(questao, num_questao)
                print(quest)
