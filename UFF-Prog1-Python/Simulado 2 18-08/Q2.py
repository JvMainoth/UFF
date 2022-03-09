#SubPrograma
def localiza(num, listaNumsFreqs):
    for i in range(len(listaNumsFreqs)):
        if listaNumsFreqs[i][0] == num:
            return i
    return None


def produz(nm):
    listaNumsFreqs = list()
    dados = open(nm, "r")
    for linha in dados:
        numero = int(linha)
        onde = localiza(numero, listaNumsFreqs)
        if onde == None:
            listaNumsFreqs.append([numero, 1])
        else:
            listaNumsFreqs[onde][1] += 1
    dados.close()
    return listaNumsFreqs

def mostrar(listaNumsFreqs):
    print("Listagem dos Números e respectivas Frequências:")
    for numero, frequencia in listaNumsFreqs:
        print(numero, "ocorre", frequencia, "vez(es)")
    print()
    return None

def moda(listaNumsFreqs):
    aModa = listaNumsFreqs[0][0]
    vezesModa = listaNumsFreqs[0][1]
    for numero, frequencia in listaNumsFreqs:
        if frequencia > vezesModa:
            vezesModa = frequencia
            aModa = numero
    return aModa

#Programa Principal
nome = input()
listaNumerosComFrequencias = produz(nome)
mostrar(listaNumerosComFrequencias)
oMaisFrequente = moda(listaNumerosComFrequencias)
print("O Mais Frequente é:", oMaisFrequente)