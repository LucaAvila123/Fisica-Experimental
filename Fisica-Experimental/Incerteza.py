import numpy as np

#valores incertezas e expoentes
variaveis = [2.5, 3.4]
incertezas = [0.5, 0.1]
expoentes = [1, -2]

#calculo do valor e incerteza
valor = np.product([var**exp for var,exp in zip(variaveis, expoentes)])
incerteza = valor * sum([np.abs(exp)*(err/var) for exp,err,var in zip(expoentes, incertezas, variaveis)])


def valorFuncao(funcao, valor, incerteza):
    return (funcao(valor + incerteza) + funcao(valor - incerteza))/2
    
def incertezaFuncao(funcao, valor, incerteza):
    return (funcao(valor + incerteza) - funcao(valor - incerteza))/2

print("Incerteza no Monomio")
print(valor)
print(incerteza)


# basta colocar uma funcao de um unico parametro numerico e retorno numerico como parametro para a funcao
valor = valorFuncao(np.sin, np.pi/2, 0.0001)
incerteza = valorFuncao(np.sin, np.pi/2, 0.0001)


print("Incerteza em uma funcao qualquer")
print(valor)
print(incerteza)