class Pessoa:
    olhos = 2

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
    kleber.sobrenome = 'Carlos'
    del kleber.filhos
    kleber.olhos = 1
    del kleber.olhos
    print(samira.__dict__)
    print(kleber.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(kleber.olhos)
    print(id(Pessoa.olhos), id(kleber.olhos), id(samira.olhos))