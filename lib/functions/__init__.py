from math import pi, sqrt

def tempo(comprimento, gravidade):
    comprimentoEmCm = comprimento
    L = comprimentoEmCm/100
    g = gravidade
    T = (2 * pi) * sqrt(L / g)
    return T


def comprimento(tempo, gravidade):
    g = gravidade
    T = tempo
    L = (T/4*(pi**2))*g
    return L