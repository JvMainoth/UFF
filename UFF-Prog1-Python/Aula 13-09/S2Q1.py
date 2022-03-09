#Subprograma
def mostra(nm):
    dados = open(nm, "r", encoding="utf-8")
    print("Conteúdo do Arquivo", nm+":")
    for linha in dados:
        print("\t", linha.strip())
    print()
    dados.close()
    return None

def insere(infos, tBrIs):
    infosA, infosB = infos.split(" X ")
    timeA, golsA = infosA.split("#")
    timeB, golsB = infosB.split("#")
    golsA, golsB = int(golsA), int(golsB)
    if timeA not in tBrIs:
        tBrIs[timeA] = {}
    if timeB not in tBrIs:
        tBrIs[timeB] = {}
    tBrIs[timeA]["Jgs"] += 1
    tBrIs[timeB]["Jgs"] += 1
    tBrIs[timeA]["GsP"] += golsA
    tBrIs[timeB]["GsP"] += golsB
    tBrIs[timeA]["GsC"] += golsB
    tBrIs[timeB]["GsC"] += golsA
    tBrIs[timeA]["SGols"] += golsA - golsB
    tBrIs[timeB]["SGols"] += golsB - golsA
    if golsA > golsB:
        tBrIs[timeA]["Pts"] += 3
        tBrIs[timeA]["Vits"] += 1
        tBrIs[timeB]["Ders"] += 1
    elif golsB > golsA:
        tBrIs[timeB]["Pts"] += 3
        tBrIs[timeB]["Vits"] += 1
        tBrIs[timeA]["Ders"] += 1
    else:
        tBrIs[timeA]["Pts"] +=1
        tBrIs[timeB]["Pts"] += 1
        tBrIs[timeB]["Emps"] += 1
        tBrIs[timeA]["Emps"] += 1
    return None

def produz(nm):
    tBrInfos = dict()
    dados = open(nm, "r", encoding="utf-8")
    for jogo in dados:
        insere(jogo.strip(), tBrInfos)
    dados.close()
    return tBrInfos

def mostraTab(tBrInfos):
    print("-"*30, "Brasileirão 2021", "-"*30)
    for time in tBrInfos:
        print("%20s" %time, tBrInfos[time])
    print("-"*78)
    return None
#Programa Principal
nome = input()
mostra(nome)
tabTimesInfosBrasileirao = produz(nome)
mostraTab(tabTimesInfosBrasileirao)