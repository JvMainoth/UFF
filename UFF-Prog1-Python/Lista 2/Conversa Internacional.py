def numTeste (teste):
    while teste > 0:
        conversa(teste)
        teste -= 1
    return None

def conversa (teste):
        linguagem = []
        pessoas = int(input())
        while pessoas > 0:
            pessoas -= 1
            linguagem.append(input())
        main = linguagem[0]
        for i in linguagem:
            if i != main:
                main = 'ingles'
                return print(main)
        return print(main)


testes = int(input())
numTeste(testes)
