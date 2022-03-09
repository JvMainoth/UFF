def mostrar(ln, lc, cv, cf):
    print("Nome:", ln)
    print("Curso:", lc)
    print("Carga Horária Efetiva:", cv)
    print("Coeficiente de Rendimento: %.2f" % cf)
    print()


def calculoChValido(ch, nt):
    nota = float(nt)
    cargaHoraria = int(ch)
    if nota >= 6:
        return cargaHoraria
    else:
        return 0


def somaCr(ch, nt):
    nota = float(nt)
    cargaHoraria = int(ch)
    return nota * cargaHoraria


def abreMatricula(lin, crMin, crMax, chMin, chMax):
    dados = open(lin, "r", encoding="utf-8")
    linhaCurso = dados.readline().strip('\n')
    linhaNome = dados.readline().strip('\n')
    chValido = 0
    chTotal = 0
    crTotal = 0
    for linha in dados:
        disciplina, semestre, cargaHoraria, nota = linha.strip('\n').split('#')
        cargaHoraria = int(cargaHoraria)
        ch = calculoChValido(cargaHoraria, nota)
        chValido += ch
        chTotal += cargaHoraria
        cr = somaCr(cargaHoraria, nota)
        crTotal += cr
    crFinal = crTotal/chTotal
    if crMin <= crFinal <= crMax and chMin <= chValido <= chMax:
        mostrar(linhaNome, linhaCurso, chValido, crFinal)


def matriculas(nm):
    dados = open(nm, "r")
    crMinimo, crMaximo = map(float, input().split())
    chMinimo, chMaximo = map(int, input().split())
    for linha in dados:
        linha = linha.strip("\n")
        abreMatricula(linha, crMinimo, crMaximo, chMinimo, chMaximo)
    dados.close()
    print()
    return None


nome = input()
matriculas(nome)

