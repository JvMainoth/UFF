#Entrada
palavras = []
frases = input().split()
while frases != []:
    #Para cada palavra em frases comparar com a lista palavras
    for palavra in frases:
        #Se a string de frases n estiver em palavras adicione
        if palavra not in palavras:
            palavras.append(palavra)
    frases = input().split()
for palavra1 in palavras:
    print(palavra1)









