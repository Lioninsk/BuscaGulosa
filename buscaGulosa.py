from Cidade import *

# h(a) = 15, h(b) = 7, h(c) = 6, h(d) = 14, h(e) = 15, h(f) = 7, h(g) = 8, h(h) = 5, h(i) = 5, h(j) = 3, h(k) = 0, h(l) = 4
cidades = {'A' : Cidade('A', 15), 'B':Cidade('B', 7), 'C':Cidade('C', 6), 'D':Cidade('D', 14), 'E':Cidade('E', 15), 'F':Cidade('F', 7),
'G':Cidade('G', 8), 'H':Cidade('H', 5), 'I':Cidade('I', 5), 'J':Cidade('J', 3), 'K':Cidade('K', 0), 'L':Cidade('L', 4)}

cidades['A'].addFilhos([cidades['B'], cidades['C'], cidades['D']])
cidades['B'].addFilhos([cidades['I'], cidades['F']])
cidades['C'].addFilho(cidades['J'])
cidades['D'].addFilho(cidades['E'])
cidades['F'].addFilho(cidades['G'])
cidades['G'].addFilho(cidades['H'])
cidades['I'].addFilho(cidades['K'])
cidades['J'].addFilho(cidades['L'])
cidades['L'].addFilho(cidades['K'])
cidades['K'].setObjetivo()


def buscaGulosa(raiz):
    print(f'{raiz}')
    if raiz.objetivo == True:
        print(f'Chegou!')
        return 
    menor = raiz.filhos[0].heuristica
    escolhido = raiz.filhos[0].nome
    for filho in raiz.filhos:
        print(f'  -Abriu:{filho}')
        if filho.heuristica < menor:
            escolhido = filho.nome
            menor = filho.heuristica
    buscaGulosa(cidades[escolhido])


    



buscaGulosa(cidades['A'])

