"""
Você deve criar uma classe carro que vai possuir dois atributos compostos por outras duas classes:

1) Motor
2) Direção

O motor terá a reponsabilidade de controlar a velocidade
Ele oferece os seguintes atributos:
1) Atributo de dado velocidade
2) Método acelerar, que deverá incrementar a velocidade em uma unidade
3) Método frear que deverá decrementar a velocidade em duas unidades

A direção terá a responsabilidade de controlar a direção. Ela oferece os seguintes atributos:
1) Valor de direção com valores possíveis: Norte, Sul, Leste, Oeste;
2) Método girar_a_direita
3) Método girar_a_esquerda

   N
 S   L
   O

   Exemplo:
   # Testando motor
   >>> motor = Motor()
   >>> motor.velocidade
   0
   >>> motor.acelerar()
   >>> motor.velocidade
   1
   >>> motor.acelerar()
   >>> motor.velocidade
   2
   >>> motor.acelerar()
   >>> motor.velocidade
   3
   >>> motor.frear()
   >>> motor.velocidade
   1
   >>> motor.frear()
   >>> motor.velocidade
   0
   # Testando direção
   >>> direcao = Direcao()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_direita()
   >>> direcao.valor
   'Norte'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Oeste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Sul'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Leste'
   >>> direcao.girar_a_esquerda()
   >>> direcao.valor
   'Norte'
   >>> carro = Carro(direcao, motor)
   >>>carro.calcular_velocidade()
   0
   >>> carro.acelerar()
   >>> carro.calcular_velocidade
   1
   >>> carro.acelerar()
   >>> carro.calcular_velocidade
   2
   >>> carro.frear()
   >>> carro.calcular_velocidade
   0
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_direita()
   >>> carro.calcular_direcao()
   'Leste'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Norte'
   >>> carro.girar_a_esquerda()
   >>> carro.calcular_direcao()
   'Oeste'
"""


class Motor:

    def __init__(self, velocidade=0):
        self.velocidade = velocidade

    def acelerar(self):
        self.velocidade = self.velocidade + 1

    def frear(self):
        self.velocidade = self.velocidade - 2
        if self.velocidade <= 0:
            self.velocidade = 0


"""
# Testando motor (Funcionou)
motor = Motor()
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.acelerar()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
motor.frear()
print(motor.velocidade)
"""


class Direcao:

    def __init__(self, rumo=0):
        self.rumo = rumo

    def virar_a_direita(self):
        self.rumo = self.rumo + 1

    def virar_a_esquerda(self):
        self.rumo = self.rumo - 1


"""
# Testando direção (Funcionou)
lista = ['Norte', 'Leste', 'Sul', 'Oeste']
direcao = Direcao()
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_direita()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
direcao.virar_a_esquerda()
print(direcao.rumo)
"""


class Carro:

    def __init__(self, motor=Motor(), direcao=Direcao()):
        self.motor = motor
        self.direcao = direcao

    def acelerar(self):
        self.motor.acelerar()

    def frear(self):
        self.motor.frear()

    def virar_a_direita(self):
        self.direcao.virar_a_direita()

    def virar_a_esquerda(self):
        self.direcao.virar_a_esquerda()

    def calcular_velocidade(self):
        print(self.motor.velocidade)

    def calcular_direção(self):
        lista = ['Norte', 'Leste', 'Sul', 'Oeste']
        var = lista[self.direcao.rumo % -4]
        print(var)


if __name__ == '__main__':
    # Testando Carro
    gol = Carro()
    gol.acelerar()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.acelerar()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.acelerar()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.acelerar()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.frear()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.acelerar()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.virar_a_direita()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.virar_a_direita()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.virar_a_direita()
    gol.calcular_velocidade()
    gol.calcular_direção()
    gol.virar_a_esquerda()
    gol.calcular_velocidade()
    gol.calcular_direção()
