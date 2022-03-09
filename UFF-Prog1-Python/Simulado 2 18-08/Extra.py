#SubPrograma
def car(lista):
    return lista[0]

def cdr(lista):
    return lista[1:]

def cons(x, lista):
    return [x]+lista

def produto(lisA, lisB):
    if lisA == []:
        return []
    else:
        return cons(car(lisA)*car(lisB), produto(cdr(lisA), cdr(lisB)))



#Programa
print(produto([3,8,2,3], [4,0,5,7]))