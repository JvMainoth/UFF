def mostrar(tProds):
    print("Conteúdo do Dicionário:")
    for chave, valor in sorted(tProds.items()):
        print("\t%6s" % (chave+" "*(6-len(chave))), valor)
    print()
    return None

def produzDicionarioPalavras(nm):
    dicionarioPsOcs = dict()  # ou {}
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        palavras = linha.strip("\n").split()
        for p in palavras:
            if p not in dicionarioPsOcs: # oudicionarioPsOcs.get(p) == None:
                dicionarioPsOcs[p] = 1
            else:
                dicionarioPsOcs[p] += 1
    dados.close()
    return dicionarioPsOcs


def produz(nm):
    dicioDicios = dict()
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        nomeArqPoema = linha.strip("\n")
        if dicioDicios.get(nomeArqPoema) == None:
            dicioDicios[nomeArqPoema] = produzDicionarioPalavras(nomeArqPoema)
        else:
            print("Já existe o Poema! ! !")
    dados.close()
    return dicioDicios








nome = input()
dicionarioDeDicionarios = produz(nome)
mostrar(dicionarioDeDicionarios)