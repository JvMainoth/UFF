def verificacao(nm):
    dados = open(nm, "r")
    linha = dados.readline().strip('\n')
    if linha == "":
        print("Arquivo vazio")
        return True
    return False


def mostrar(nm, msgFormatada):
    print(msgFormatada % nm)
    dados = open(nm, "r")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None


def circulo(x, y, r, nm):
    from os import remove, rename
    dados = open(nm, "r")
    temp = open(nm+"$$$", "w")
    circuloXmin = x - r
    circuloXmax = x + r
    circuloYmin = y - r
    circuloYmax = y + r
    for linha in dados:
        arquivoX, arquivoY = map(int, linha.split())
        if circuloXmin <= arquivoX <= circuloXmax and circuloYmin <= arquivoY <= circuloYmax:
            continue
        else:
            temp.write(linha)
    temp.close()
    dados.close()
    remove(nm)
    rename(nm + "$$$", nm)
    return None


nome = input()
veri = verificacao(nome)
if veri is False:
    mostrar(nome, "Pontos do Arquivo %s antes das remoções:")
    xC, yC, raio = map(int, input().split())
    circulo(xC, yC, raio, nome)
    mostrar(nome, "Pontos do Arquivo %s depois das eventuais remoções:")
