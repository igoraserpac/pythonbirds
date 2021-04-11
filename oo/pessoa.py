class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá! {id(self)}'


if __name__ == '__main__':
    igor = Pessoa(nome='Igor')
    alonso = Pessoa(igor, nome='Alonso')
    print(Pessoa.cumprimentar(alonso))
    print(id(alonso))
    print(alonso.cumprimentar())
    print(alonso.nome)
    print(alonso.idade)
    for filho in alonso.filhos:
        print(filho.nome)
    alonso.sobrenome = 'Cunha'
    del alonso.filhos
    alonso.olhos = 1
    del alonso.olhos
    print(alonso.__dict__)
    print(igor.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(alonso.olhos)
    print(igor.olhos)
    print(id(alonso.olhos), id(igor.olhos), id(Pessoa.olhos))
