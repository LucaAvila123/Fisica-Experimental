tempoSemPeso = [2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490]
tempoComPeso = [2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205]

# calculando tempo médio
tempoTotalSemPeso = 0
for i in range tempoSemPeso:
    tempoTotalSemPeso += tempoSemPeso[i]

tempoMedioSemPeso = tempoTotalSemPeso / length(tempoSemPeso)

tempoTotalComPeso = 0
for i in range tempoComPeso:
    tempoTotalComPeso += tempoComPeso[i]

tempoMedioComPeso = tempoTotalComPeso / length(tempoComPeso)

# calculando as incertezas (incluindo operacao para ter apenas números positivos no somatório)
incertezaTempoSemPeso = 0

for i in range tempoSemPeso:
    incertezaTempoSemPeso += tempoMedioSemPeso - tempoSemPeso[i] if tempoMedioSemPeso > tempoSemPeso[i] else tempoSemPeso[i] - tempoMedioSemPeso
    
incertezaTempoSemPeso /= length(tempoSemPeso)

incertezaTempoComPeso = 0

for i in range tempoComPeso:
    incertezaTempoComPeso += tempoMedioComPeso - tempoComPeso[i] if tempoMedioComPeso > tempoComPeso[i] else tempoComPeso[i] - tempoMedioComPeso

incertezaTempoComPeso /= length(tempoComPeso)
