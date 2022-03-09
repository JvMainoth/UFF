#Programa
#Subprograma
def listaCasaveis(nmCli, prefsCli, qtd, nmCadastro):
    print("Listagem dos Casáveis com", nmCli)
    print("Quantidade Mínima de Preferências em Comum", qtd)
    dados = open(nmCadastro, "r", encoding='utf-8')
    for linha in dados:
        infos = linha.strip('\n').split('#')
        nomeCandidato = infos[0]
        prefsCandidato = set(infos[1:])
        prefsComuns = prefsCli.intersection(prefsCandidato)
        if len(prefsComuns) >= qtd:
            print(nomeCandidato)
    dados.close()
    print()
    return None

#Principal
nomeCliente = input()
preferenciasCliente = set(input().split("#"))
qtdComuns = int(input())
nomeCadastrados = input()
listaCasaveis(nomeCliente, preferenciasCliente, qtdComuns, nomeCadastrados)