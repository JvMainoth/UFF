# Programa Agrupa Pontos do Espaço 2D
# Subprogramas
def mostrar(nm):
    dados = open(nm, "r")
    print(nm+":")
    x, y = tuple(map(int, dados.readline().split()))
    while (x, y) != (0, 0):
        print("\t", (x, y))
        x, y = tuple(map(int, dados.readline().split()))
    dados.close()
    print()
    return None

def centroide(g):
    somaX = somaY = 0
    for x, y in g:
        somaX += x
        somaY += y
    return somaX/len(g), somaY/len(g)





def distancia(xP, yP, grupo):
    if grupo == None:
        return 0
    else:
        xCentroide, yCentroide = centroide(grupo)
        return ((xCentroide - xP) ** 2 + (yCentroide - yP) ** 2) ** 0.5





def achaGrupoMaisProximo(xPt, yPt, lisGs):
    posVencedor = 0
    distVencedor = distancia(xPt, yPt, lisGs[0])
    for pos in range(1, len(lisGs)):
        distAtual = distancia(xPt, yPt, lisGs[pos])
        if distAtual < distVencedor:
            distVencedor = distAtual
            posVencedor = pos
    return posVencedor




def agrupa(qGs, nmPts):
    listaGs = [None] * qGs
    dados = open(nmPts, "r")
    x, y = tuple(map(int, dados.readline().split()))
    while (x, y) != (0, 0):
        posGrupo = achaGrupoMaisProximo(x, y, listaGs)
        if listaGs[posGrupo] == None:
            listaGs[posGrupo] = [(x, y)]
        else:
            listaGs[posGrupo].append((x, y))
        x, y = tuple(map(int, dados.readline().split()))
    dados.close()
    return listaGs

def mostrarGps(listaGs):
    print('Grupos')
    for g in listaGs:
        print("\t", g)
    print()
    return None

# Principal
nomeArqPontos = input()
qtdGrupos = int(input())
mostrar(nomeArqPontos)
grupos = agrupa(qtdGrupos, nomeArqPontos)
mostrarGps(grupos)