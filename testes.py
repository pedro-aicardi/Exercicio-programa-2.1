import random
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

        
dicionario = {
  "facil": [
    {
      "titulo": "Qual o resultado da operação 57 + 32?",
      "nivel": "facil",
      "opcoes": {
        "A": "-19",
        "B": "85",
        "C": "89",
        "D": "99"
      },
      "correta": "C"
    },
    {
      "titulo": "Qual destes parques não se localiza em São Paulo?!",
      "nivel": "facil",
      "opcoes": {
        "A": "Ibirapuera",
        "B": "Parque do Carmo",
        "C": "Parque Villa Lobos",
        "D": "Morro da Urca"
      },
      "correta": "D"
    },
    {
      "titulo": "Qual destas não é uma linguagem de programação?",
      "nivel": "facil",
      "opcoes": {
        "A": "Miratdes",
        "B": "Python",
        "C": "Lua",
        "D": "C++"
      },
      "correta": "A"
    },
    {
      "titulo": "Dentre os listados, qual destes esportes é menos praticado no Brasil?",
      "nivel": "facil",
      "opcoes": {
        "A": "Natação",
        "B": "Vôlei",
        "C": "Ski Cross Country",
        "D": "Natação"
      },
      "correta": "C"
    }
  ],
  "medio": [
    {
      "titulo": "Qual destes números é primo?",
      "nivel": "medio",
      "opcoes": {
        "A": "259",
        "B": "85",
        "C": "49",
        "D": "19"
      },
      "correta": "D"
    },
    {
      "titulo": "Na Conjectura de _______, escolhendo-se um número natural inicial n, onde n > 0, os seguintes critérios serão obedecidos: Se n for par o seu sucessor será a metade e se n for ímpar o seu sucessor será o triplo mais um, gerando então um novo número. Qual o nome da conjectura?",
      "nivel": "medio",
      "opcoes": {
        "A": "Collatz",
        "B": "Goldbach",
        "C": "Poincaré",
        "D": "Hodge"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual a segunda pessoa mais seguida no Instagram?",
      "nivel": "medio",
      "opcoes": {
        "A": "Cristiano Ronaldo",
        "B": "Dwayne Johnson",
        "C": "Kim Kardashian",
        "D": "Kylie Jenner"
      },
      "correta": "D"
    }
  ],
  "dificil": [
    {
      "titulo": "A reprodução dos seres vivos é um processo biológico através do qual os organismos geram descendência. Qual desta não é uma forma de reprodução assexuada?",
      "nivel": "dificil",
      "opcoes": {
        "A": "Autogamia",
        "B": "Esporulação",
        "C": "Partenogênese",
        "D": "Divisão binária"
      },
      "correta": "A"
    },
    {
      "titulo": "Qual o resultado da operação 5 + 2 * 3 ^ 2, onde ^ representa potenciação?",
      "nivel": "dificil",
      "opcoes": {
        "A": "441",
        "B": "86",
        "C": "Nenhuma das outras respostas",
        "D": "23"
      },
      "correta": "D"
    }
  ]
}

nivel ='medio'


questoes_sorteadas = [
  {
    "titulo": "Qual destes parques não se localiza em São Paulo?!",
    "nivel": "facil",
    "opcoes": {
      "A": "Ibirapuera",
      "B": "Parque do Carmo",
      "C": "Parque Villa Lobos",
      "D": "Morro da Urca"
    },
    "correta": "D"
  },
  {
    "titulo": "Qual o resultado da operação 57 + 32?",
    "nivel": "facil",
    "opcoes": {
      "A": "-19",
      "B": "85",
      "C": "89",
      "D": "99"
    },
    "correta": "C"
  },
  {
    "titulo": "Qual destes números é primo?",
    "nivel": "medio",
    "opcoes": {
      "A": "259",
      "B": "85",
      "C": "49",
      "D": "19"
    },
    "correta": "D"
  }
]

print(sorteia_questao_inedita(dicionario, nivel,questoes_sorteadas))



lista = [{}, {}, {}]
for i in range(0, len(lista)):
  tamanho = len(lista[0])
  if tamanho == 0:
    x = True
  else:
    x = False
print(x)

for i in range(0, 10):
  print(i)