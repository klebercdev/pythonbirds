class Pessoa:
    def __init__(self, *filhos, nome=None, idade=41):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)
    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__ == '__main__':
    samira = Pessoa(nome='Samira')
    kleber = Pessoa(samira, nome='Kleber')
    print(Pessoa.cumprimentar(kleber))
    print(id(kleber))
    print(kleber.cumprimentar())
    print(kleber.nome)
    print(kleber.idade)
    for filho in kleber.filhos:
        print(filho.nome)
