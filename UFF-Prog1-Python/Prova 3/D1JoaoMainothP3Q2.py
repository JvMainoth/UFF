def produz(tMin, tMax, nm):
    dicionarioPro = {}
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        codigo, produto, quantidade, preco = linha.strip('\n').split('#')
        preco = float(preco)
        quantidade = int(quantidade)
        if tMin <= preco <= tMax:
            dicionarioPro[codigo] = []
            dicionarioPro[codigo] = [produto, quantidade, preco]
    dados.close()
    return dicionarioPro

def formatacao(dictPro):
    for i in sorted(dictPro.keys()):
        print(f"Código: {i:<10} Descrição: {dictPro[i][0]:<25} Qtd: {dictPro[i][1]:<10} Preço: {dictPro[i][2]}")



nome = input()
tamMin, tamMax = map(float, input().split())
dicionarioPro = produz(tamMin, tamMax, nome)
formatacao(dicionarioPro)