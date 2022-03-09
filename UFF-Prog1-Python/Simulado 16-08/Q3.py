def mostrar(nm, formatacao):
    print(formatacao % nm)
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        print(linha.strip("\n"))
    dados.close()
    print()
    return None

def produz(nm, nmDuas):
    dados = open(nm, "r", encoding="utf-8")
    dadosDuas = open(nmDuas, "w", encoding="utf-8")
    for linha in dados:
        nome, tipo, dose = linha.strip('\n').split('#')
        if dose == '2':
            dadosDuas.write(nome+'#'+tipo+'\n')
    dadosDuas.close()
    dados.close()
    return None

def pertence(n, nm):
    dados = open(nm, "r", encoding="utf-8")
    for linha in dados:
        nome, tipo = linha.split("#")
        if n == nome:
            dados.close()
            return True
    dados.close()
    return False


def dividir(nm, nm2, nm1C, nm10):
    produz(nm, nm2)
    dados = open(nm, "r", encoding="utf-8")
    dadosUmaCorona = open(nm1C, "w", encoding="utf-8")
    dadosUmaOxford = open(nm10, "w", encoding="utf-8")
    for linha in dados:
        nome, tipo, dose = linha.strip("\n").split("#")
        if not pertence(nome, nm2):
            if tipo == "coronavac":
                dadosUmaCorona.write(linha)
            else:
                dadosUmaOxford.write(linha)
    dadosUmaCorona.close()
    dadosUmaOxford.close()
    dados.close()
    return None

#Principal
nome = input()
mostrar(nome, "Conteúdo do Arquivo de Vacinas %s:")
nomeDuasDoses, nomeUmaCoronavac, nomeUmaOxford = input().split()
dividir(nome, nomeDuasDoses, nomeUmaCoronavac, nomeUmaOxford)
mostrar(nomeDuasDoses, "Vacinados com Duas Doses em %s:")
mostrar(nomeUmaCoronavac, "Vacinados com Uma Dose em %s:")
mostrar(nomeUmaOxford, "Vacinados com Uma Dose em %s:")