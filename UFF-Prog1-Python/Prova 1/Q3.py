
#Opções
palavras = []
frases = input().split('#')
while frases != ['Fim das Opções']:
    for i in frases:
        palavras.append(i.split())
    frases = input().split('#')

periodosduplos = []
periodos = map(int, input().split())
while periodos != 'Fim dos Períodos':
    for i in periodos:
        listatemporaria = []
        listatemporaria.append(i)
    periodosduplos.append(listatemporaria)
    periodos = map(int, input().split())





