#Programa - Pontos Mais Distantes
#SubPrograma
def mostrar(nm, msgFormatada):
    print(msgFormatada % nm)
    dados = open(nm, "r")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None

def distancia(pA, pB):
    return ((pB[0] - pA[0])**2+(pB[1]-pA[1])**2)**0.5

def achaMaisDistante(pt, nm):
    dados = open(nm, "r")
    linha = dados.readline()
    pMD = tuple(map(int, linha.split()))
    dPtPMD = distancia(pt, pMD)
    for linha in dados:
        pAtual = tuple(map(int, linha.split()))
        dPtPAtual = distancia(pt, pAtual)
        if dPtPAtual > dPtPMD:
            dPtPMD = dPtPAtual
            pMD = pAtual
    dados.close()
    return pMD, dPtPMD



def achaMaisDistantes(nm):
    dados = open(nm, "r")
    linha = dados.readline() #aqui pega a primeira linha
    pA = pB = tuple(map(int, linha.split())) #mapeando de 2 em 2 na forma de tupla e transformando em INT
    dAB = 0
    for linha in dados: #por conta do readline anterior esse passou para a outra linha no caso "150 250"
        pAtual = tuple(map(int, linha.split()))
        pMaisDistanteAtual, distAtualOutro = achaMaisDistante(pAtual, nm)
        if distAtualOutro > dAB:
            dAB = distAtualOutro
            pA = pAtual
            pB = pMaisDistanteAtual
    dados.close()
    return pA, pB, dAB
#Programa
nome = input()
mostrar(nome, 'Conteúdo do Arquivo de Pontos %s:')
pontoA, pontoB, distanciaAB = achaMaisDistantes(nome)
print('Pontos Mais Distantes:', pontoA, "e", pontoB, "com distância = %.2f" % distanciaAB)