tempoSemPesoFinal = [2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490]
tempoComPesoFinal = [2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205]

arrayValoresCalculadosSemPesoFinal = [0, 0, 0, 0]
arrayValoresCalculadosComPesoFinal = [0, 0, 0, 0]

def calculaTempos(arrayDeTempo, tempoMedio, incertezaTempo, tempoMedioQuadrado, incertezaTempoQuadrado):
    # calculando tempo médio
    tempoTotal = 0
    tempoTotalQuadrado = 0

    for i in range(10):
        tempoTotal += arrayDeTempo[i]
        tempoTotalQuadrado += arrayDeTempo[i]**2

    tempoMedio = tempoTotal / 10
    tempoMedioQuadrado = tempoTotalQuadrado / 10


    # calculando as incertezas (incluindo operacao para ter apenas números positivos no somatório)
    incertezaTempo = 0
    incertezaTempoQuadrado = 0
    
    for i in range(10):
        incertezaTempo += tempoMedio - arrayDeTempo[i] if tempoMedio > arrayDeTempo[i] else arrayDeTempo[i] - tempoMedio
        incertezaTempoQuadrado += tempoMedioQuadrado - arrayDeTempo[i]**2 if tempoMedioQuadrado > arrayDeTempo[i]**2 else arrayDeTempo[i]**2 - tempoMedioQuadrado
        
    incertezaTempo /= 10
    incertezaTempoQuadrado /= 10

calculaTempos(tempoSemPesoFinal, arrayValoresCalculadosSemPesoFinal[0], arrayValoresCalculadosSemPesoFinal[1], arrayValoresCalculadosSemPesoFinal[2], arrayValoresCalculadosSemPesoFinal[3])
calculaTempos(tempoComPesoFinal, arrayValoresCalculadosComPesoFinal[0], arrayValoresCalculadosComPesoFinal[1], arrayValoresCalculadosComPesoFinal[2], arrayValoresCalculadosComPesoFinal[3])

print(f"Tempo médio sem peso e incerteza: {arrayValoresCalculadosSemPesoFinal[0]}  {arrayValoresCalculadosSemPesoFinal[1]}")
print(f"Tempo médio sem peso ao quadrado e incerteza: {arrayValoresCalculadosSemPesoFinal[2]} {arrayValoresCalculadosSemPesoFinal[3]}")
print(f"Tempo médio com peso e incerteza: {arrayValoresCalculadosComPesoFinal[0]}  {arrayValoresCalculadosComPesoFinal[1]}")
print(f"Tempo médio com peso ao quadrado e incerteza: {arrayValoresCalculadosComPesoFinal[2]} {arrayValoresCalculadosComPesoFinal[3]}")