# Programa Editor de Arquivo Texto
#Subprograma
def menu(listaOps):
    for op in listaOps:
        print(op)
    return int(input('Escolha:/>'))


def mostrarArquivo(nome):
    dados = open(nome, 'r', encoding='utf-8')
    linha = dados.readline()
    while linha  != '':
        print(linha, end='')
        linha = dados.readline()
    dados.close()
    print()
    return None

def criarArquivo(nome):
    dados = open(nome, 'w', encoding='utf-8')
    dados.close()
    return None

def destruirArquivo(nome):
    from os import remove
    remove(nome)
    return None

def anexarLinhaEmArquivo(nome):
    linhaNova = input()
    dados = open(nome, 'a', encoding='utf-8')
    dados.write(linhaNova+'\n')
    dados.close()
    return None

def inserirNovaLinhaEmPosicao(nome):
    #usando simstam operacional
    from os import remove, rename
    novaLinha = input()
    posicao = int(input())
    dados = open(nome, 'r', encoding='utf-8')
    temporario = open(nome+'$$$', 'w', encoding='utf-8')
    posAtual = 0
    for linha in dados:
        posAtual += 1
        if posicao == posAtual:
            temporario.write(novaLinha+'\n')
        temporario.write(linha)
    if posicao > posAtual:
        temporario.write(novaLinha+'\n')
    temporario.close()
    dados.close()
    remove(nome)
    rename(nome+'$$$', nome)
    return None

def removerLinhaEmPosicao(nome):
    from os import remove, rename
    posicao = int(input())
    dados = open(nome, 'r', encoding='utf-8')
    temporario = open(nome+'$$$', 'w', encoding='utf-8')
    posAtual = 0
    for linha in dados:
        posAtual += 1
        if posicao != posAtual:
            temporario.write(linha)
    if posicao > posAtual:
        print('Erro - linha inexistente!!!')
    temporario.close()
    dados.close()
    remove(nome)
    rename(nome+'$$$', nome)
    return None




#Principal
OPS = ['(0) Conectar', '(1) Mostrar', '(2) Criar', '(3) Destruir', '(4) Anexar Linha no Fim',
       '(5) Inserir Linha Nova em Posição', '(6) Remover Linha em Posição', '(9) Sair']
nomeArquivo = 'default.txt'
criarArquivo(nomeArquivo)
opcao = menu(OPS)
while opcao != 9:
    if opcao == 0:
        nomeArquivo = input()
    elif opcao == 1:
        mostrarArquivo(nomeArquivo)
    elif opcao == 2:
        criarArquivo(nomeArquivo)
    elif opcao == 3:
        destruirArquivo(nomeArquivo)
    elif opcao == 4:
        anexarLinhaEmArquivo(nomeArquivo)
    elif opcao == 5:
        inserirNovaLinhaEmPosicao(nomeArquivo)
    elif opcao == 6:
        removerLinhaEmPosicao(nomeArquivo)
    opcao = menu(OPS)