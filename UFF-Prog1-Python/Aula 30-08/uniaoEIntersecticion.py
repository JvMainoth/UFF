def produz(nm):
    conjPals = set()
    dados = open(nm, "r", encoding = "utf-8")
    for linha in dados:
        pals = linha.strip("\n").split()
        for p in pals:
            conjPals.add(p)
    dados.close()
    return conjPals


def mostrar(conjunto, msg):
    print("Conjunto %s:" %msg)
    lista = sorted(conjunto)
    print(lista)
    for item in lista:
        print(item)
    print()
    return None







nomeA, nomeB = input().split()
conjuntoA = produz(nomeA)
conjuntoB = produz(nomeB)
mostrar(conjuntoA, nomeA)
mostrar(conjuntoB, nomeB)
intersecaoAB = conjuntoA.intersection(conjuntoB)
mostrar(intersecaoAB, "Interseção"+nomeA+" com "+nomeB)
uniaoAB = conjuntoA.union(conjuntoB)
mostrar(uniaoAB, "União" +nomeA+" com "+nomeB)