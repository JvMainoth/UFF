#Subprograma
def extremos(nm):
    dados = open(nm, "r")
    linha = dados.readline()
    if linha == "":
        menor = maior = None
    else:
        menor = maior = float(linha)
        for linha in dados:
            numero = float(linha)
            if numero < menor:
                menor = numero
            elif numero > maior:
                maior = numero
    dados.close()
    return menor, maior
#Programa Principal
nome = input()
oMenor, oMaior = extremos(nome)
if oMenor == oMaior == None:
    print("Arquivo Vazio - sem extremos.")
else:
    print("O Menor Elemento: ", oMenor, "e o Maior Elemento: ", oMaior)