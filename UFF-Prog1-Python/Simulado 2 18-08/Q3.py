#SubPrograma
def mostrar(nm, formatacao):
    print(formatacao%nm)
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None

def dividir(nm, nmVogais, nmOutros):
    dados = open(nm, "r", encoding="utf-8")
    dadosVogais = open(nmVogais, "w", encoding="utf-8")
    dadosOutros = open(nmOutros, "w", encoding="utf-8")
    for linha in dados:
        if linha[0].upper() in "AEIOUÁÉÍÓÚÂÊÎÔÛÃÕ":
            dadosVogais.write(linha)
        else:
            dadosOutros.write(linha)
    dadosOutros.close()
    dadosVogais.close()
    dados.close()
    return None

#Programa
nome = input()
nomesVogais, nomesOutros = input().split()
dividir(nome, nomesVogais, nomesOutros)
mostrar(nomesVogais, "Iniciados com Vogais %s: ")
mostrar(nomesOutros, "Outros caracteres %s: ")