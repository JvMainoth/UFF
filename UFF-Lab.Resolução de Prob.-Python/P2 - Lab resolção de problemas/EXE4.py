import sys

def acharItens(diasCho,fran,temp):
    achados = 0
    for i in range(fran):
        achados += temp//diasCho[i]
    return achados


def procuraBinaria(diasCho, cho, fran, maior):
    menor = 1
    while menor < maior:
        meio = (menor + maior) >> 1
        item = acharItens(diasCho, cho, meio)
        if item < fran:
            menor = meio + 1
        else:
            maior = meio
    return maior

def tempoMin(diasCho, cho, fran):
    valorMaximo = -sys.maxsize
    for i in range(cho):
        valorMaximo = max(valorMaximo, diasCho[i])
    return procuraBinaria(diasCho, cho, fran, valorMaximo * fran)


chocadeiras, frangos = map(int, input().split())
diasChocadeiras = list(map(int, input().split()))
print(tempoMin(diasChocadeiras, chocadeiras, frangos))
