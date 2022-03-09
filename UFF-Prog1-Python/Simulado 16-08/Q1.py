#Programa P21Q1 - Maior e Decremento
#Subprograma
def mostrar(nm, msgFormatada):
    print(msgFormatada % nm)
    dados = open(nm, "r")
    for linha in dados:
        print(linha.strip("\n")) #retira o \n da linha
    dados.close()
    print()
    return None


def achaMaiorNaLinha(numeros):
    if numeros == []:
        valorMaior = None
    else:
        valorMaior = numeros[0]  # pega o primeiro número da linha
        for valor in numeros:
            if valor > valorMaior:  # compara com o prox
                valorMaior = valor  # se for maior o valorMaior pega o valor
    return valorMaior


def achaMaior(nm):
    dados = open(nm, "r")  #abri o arquivo e "r" bota em modo leitura.
    linha = dados.readline() #vai pegar a primeira do documento com \n
    if linha == "":
        oMaior = None
    else:
        oMaior = int(linha.split()[0]) #converte em inteiro a linha splitada (10) por conta do split marcado com o [0]
        while linha != "":
            maiorNaLinha = achaMaiorNaLinha(list(map(int, linha.split()))) #separa tudo na linha e transforma em INT
            if maiorNaLinha > oMaior:
                oMaior = maiorNaLinha
            linha = dados.readline() # e le a proxima linha
    dados.close()
    return oMaior

def decrementa(nm, oMaior):
    from os import remove, rename #apagar e renomear
    dados = open(nm, "r")
    temp = open(nm+'$$$', 'w')
    for linha in dados:
        numeros = list(map(int, linha.split()))
        linhaMudada = ""
        for num in numeros:
            if num == oMaior:
                linhaMudada += str(num-1)+" "
            else:
                linhaMudada += str(num) + " "
        linhaMudada = linhaMudada[0:len(linhaMudada)-1] #corrigi o ultimo espaço em branco
        temp.write(linhaMudada+"\n")
    temp.close()
    dados.close()
    remove(nm) #apaga o anterior
    rename(nm+"$$$", nm) #renomeia o novo e modificado pelo antigo
    return None

#principal
nome = input()
maiorValor = achaMaior(nome)
print("Maior Valor Encontrado:", maiorValor)
mostrar(nome, "Conteúdo de %s antes do Decremento:")
decrementa(nome, maiorValor)
mostrar(nome, "Conteúdo de %s após do Decremento:")