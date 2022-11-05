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
                dicio2['correta']='valor_errado'
    if dicio_principal != dicio2:
        return dicio2
    else:
        return {}