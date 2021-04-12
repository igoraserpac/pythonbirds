class Pessoa:  # Classe Pessoa
    olhos = 2  # Atributo de classe

    def __init__(self, *filhos, nome=None, idade=35):  # Atributos
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}. '

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_de_classe=super().cumprimentar()
        return f'{cumprimentar_de_classe}Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    igor = Mutante(nome='Igor')
    alonso = Homem(igor, nome='Alonso')
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
    print(Pessoa.olhos)
    print(alonso.olhos)
    print(igor.olhos)
    print(id(alonso.olhos), id(igor.olhos), id(Pessoa.olhos))
    print(Pessoa.metodo_estatico(), alonso.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), alonso.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(igor, Pessoa))
    print(isinstance(igor, Homem))
    print(igor.olhos)
    print(alonso.cumprimentar())
    print(igor.cumprimentar())
