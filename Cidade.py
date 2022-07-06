class Cidade:
    def __init__(self, nome, heuristica) -> None:
        self.nome = nome
        self.heuristica = heuristica
        self.filhos = []
        self.objetivo = False

    def __str__(self) -> str:
        return f'{self.nome} - valor:{self.heuristica}'

    def setObjetivo(self) -> None:
        self.objetivo = True
    
    def addFilhos(self, filhos) -> None:
        for filho in filhos:
            self.filhos.append(filho)
    
    def addFilho(self, filho) -> None:
        self.filhos.append(filho)
    


    


