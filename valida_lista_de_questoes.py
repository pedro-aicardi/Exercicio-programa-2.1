from valida_questao import *

def valida_questoes(lista_questoes):
    lista = []
    for i in range(0, len(lista_questoes)):
        dicio = lista_questoes[i]
        valida = valida_questao(dicio)
        lista.append(valida)
    return lista
