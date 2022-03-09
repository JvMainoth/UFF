#Subprograma
def carrega(nm):
    tProds = dict()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        cod, desc, qtd, pre = linha.strip("\n").split("#")
        qtd = int(qtd)
        pre = float(pre)
        if cod in tProds:
            print("Já existe este produto na tabela. Confira", cod)
        else:
            tProds[cod] = (desc, qtd, pre)
    dados.close()
    return tProds

def mostrar(tProds):
    print("Conteúdo da Tabela:")
    for chave, valor in sorted(tProds.items()):
        print("\t%6s" % (chave+" "*(6-len(chave))), valor)
    print()
    return None

#Principal
nome = input()
tabProdutos = carrega(nome)
mostrar(tabProdutos)