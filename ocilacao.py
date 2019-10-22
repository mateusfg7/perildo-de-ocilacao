from math import pi, sqrt
from sys import argv as param


try:
    parametroUm = param[1]
    parametroDois = param[2]
    parametroTres = float(param[3])
except IndexError:
    print("Número de argumentos insuficientes!")
    exit()
except ValueError:
        print("Valor inválido ou inexistente!")
        exit()


def Tempo(comprimento, gravidade):
    comprimentoEmCm = comprimento
    L = comprimentoEmCm/100
    g = gravidade
    T = (2 * pi) * sqrt(L / g)
    print("T ≅ {:.5f}s".format(T))

def Comprimento(tempo, gravidade):
    g = gravidade
    T = tempo
    L = (T/4*(pi**2))*g
    print("L ≅ {:.5f}cm".format(L))

def Astro():
    astros = {
        "sol": 274.13,
        "mercurio": 3.78,
        "venus": 8.60,
        "terra": 9.8,
        "marte": 3.72,
        "jupiter": 24.8,
        "saturno": 10.5,
        "urano": 8.5,
        "netuno": 10.8,
        "plutao": 5.88,
        "lua": 1.67
    }

    if parametroDois == 'sol':
        return astros['sol']
    elif parametroDois == 'mer':
        return astros['mercurio']
    elif parametroDois == 'ven':
        return astros['venus']
    elif parametroDois == 'ter':
        return astros['terra']
    elif parametroDois == 'mar':
        return astros['marte']
    elif parametroDois == 'jup':
        return astros['jupiter']
    elif parametroDois == 'sat':
        return astros['saturno']
    elif parametroDois == 'ura':
        return astros['urano']
    elif parametroDois == 'net':
        return astros['netuno']
    elif parametroDois == 'plu':
        return astros['plutao']
    elif parametroDois == 'lua':
        return astros['lua']



if parametroUm == "t":
    Tempo(parametroTres, Astro())
elif parametroUm == "c":
    Comprimento(parametroTres, Astro())