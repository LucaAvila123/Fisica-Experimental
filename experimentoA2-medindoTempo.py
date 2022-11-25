tempoSemPesoFinal = [2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490]
tempoComPesoFinal = [2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205]

# calculando tempo médio
tempoTotalSemPesoFinal = 0
tempoTotalSemPesoQuadradoFinal = 0
tempoTotalComPesoFinal = 0
tempoTotalComPesoQuadradoFinal = 0

for i in range(10):
    tempoTotalSemPesoFinal += tempoSemPesoFinal[i]
    tempoTotalSemPesoQuadradoFinal += tempoSemPesoFinal[i]**2
    tempoTotalComPesoFinal += tempoComPesoFinal[i]
    tempoTotalComPesoQuadradoFinal += tempoComPesoFinal[i]**2


tempoMedioSemPesoFinal = tempoTotalSemPesoFinal / 10
tempoMedioSemPesoQuadrado = tempoTotalSemPesoQuadradoFinal / 10
tempoMedioComPesoFinal = tempoTotalComPesoFinal / 10
tempoMedioComPesoQuadrado = tempoTotalComPesoQuadradoFinal / 10


# calculando as incertezas (incluindo operacao para ter apenas números positivos no somatório)
incertezaTempoSemPesoFinal = 0
incertezaTempoSemPesoQuadradoFinal = 0
incertezaTempoComPesoFinal = 0
incertezaTempoComPesoQuadradoFinal = 0
for i in range(10):
    incertezaTempoSemPesoFinal += tempoMedioSemPesoFinal - tempoSemPesoFinal[i] if tempoMedioSemPesoFinal > tempoSemPesoFinal[i] else tempoSemPesoFinal[i] - tempoMedioSemPesoFinal
    incertezaTempoSemPesoQuadradoFinal += tempoMedioSemPesoQuadrado - tempoSemPesoFinal[i]**2 if tempoMedioSemPesoQuadrado > tempoSemPesoFinal[i]**2 else tempoSemPesoFinal[i]**2 - tempoMedioSemPesoQuadrado
    incertezaTempoComPesoFinal += tempoMedioComPesoFinal - tempoComPesoFinal[i] if tempoMedioComPesoFinal > tempoComPesoFinal[i] else tempoComPesoFinal[i] - tempoMedioComPesoFinal
    incertezaTempoComPesoQuadradoFinal += tempoMedioComPesoQuadrado - tempoComPesoFinal[i]**2 if tempoMedioComPesoQuadrado > tempoComPesoFinal[i]**2 else tempoComPesoFinal[i]**2 - tempoMedioComPesoQuadrado
    

incertezaTempoSemPesoFinal /= 10
incertezaTempoSemPesoQuadradoFinal /= 10
incertezaTempoComPesoFinal /= 10
incertezaTempoComPesoQuadradoFinal /= 10

print(f"Tempo médio sem peso e incerteza: {tempoMedioSemPesoFinal}  {incertezaTempoSemPesoFinal}")
print(f"Tempo médio sem peso ao quadrado e incerteza: {tempoMedioSemPesoQuadrado} {incertezaTempoSemPesoQuadradoFinal}")
print(f"Tempo médio com peso e incerteza: {tempoMedioComPesoFinal}  {incertezaTempoComPesoFinal}")
print(f"Tempo médio com peso ao quadrado e incerteza: {tempoMedioComPesoQuadrado} {incertezaTempoComPesoQuadradoFinal}")

