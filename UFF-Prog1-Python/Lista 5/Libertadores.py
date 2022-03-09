def numTestes(test):
    while test > 0:
        test -= 1
        liberta()
    return None

def liberta():
    pontostimeCasa = 0
    pontostimeVisitante = 0
    casa1, c, visitante1 = map(str, input().split())
    visitante2, c, casa2 = map(str, input().split())
    if casa1 > visitante1:
        pontostimeCasa += 3
    elif visitante1 > casa1:
        pontostimeVisitante +=3
    else:
        pontostimeCasa += 1
        pontostimeVisitante += 1
    if visitante2 > casa2:
        pontostimeVisitante += 3
    elif casa2 > visitante2:
        pontostimeCasa +=3
    else:
        pontostimeCasa += 1
        pontostimeVisitante += 1
    saldoTimeCasa = (int(casa1) + int(casa2)) - (int(visitante1) + int(visitante2))
    saldoTimeVisitante = (int(visitante1) + int(visitante2)) - (int(casa1) + int(casa2))
    golsForadeCasaCasa = casa2
    golsForadeCasaVisitante = visitante1





    if pontostimeCasa > pontostimeVisitante:
        print("Time 1")
    elif pontostimeVisitante > pontostimeCasa:
        print("Time 2")
    else:
        if saldoTimeCasa > saldoTimeVisitante:
            print("Time 1")
        elif saldoTimeVisitante > saldoTimeCasa:
            print("Time 2")
        else:
            if golsForadeCasaCasa > golsForadeCasaVisitante:
                print("Time 1")
            elif golsForadeCasaVisitante > golsForadeCasaCasa:
                print("Time 2")
            else:
                print("Penaltis")


testes = int(input())
numTestes(testes)