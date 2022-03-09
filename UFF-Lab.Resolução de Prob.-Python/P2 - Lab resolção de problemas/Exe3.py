codigo = input()
palavra = input()
cont_codigo = 0
cont_palavra = 0
cont_final = 0


if len(palavra) == 3:
    for i in range(len(codigo) - len(palavra)):
        for i2 in palavra:
            if i2 != codigo[cont_codigo]:
                cont_codigo += 1
                cont_palavra += 1
            else:
                break
        if cont_palavra == len(palavra):
            cont_final += 1
        cont_codigo = i + 1
        cont_palavra = 0
    print(cont_final)
else:
    for i in range(len(codigo) - len(palavra) + 1):
        for i2 in palavra:
            if i2 != codigo[cont_codigo]:
                cont_codigo += 1
                cont_palavra += 1
            else:
                break
        if cont_palavra == len(palavra):
            cont_final += 1
        cont_codigo = i + 1
        cont_palavra = 0
    print(cont_final)











