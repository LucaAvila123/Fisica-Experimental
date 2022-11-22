tempoSemPeso = [2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490]
tempoComPeso = [2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205]

# calculando tempo médio
tempoTotalSemPeso = 0
for i in range(10):
    tempoTotalSemPeso += tempoSemPeso[i]

tempoMedioSemPeso = tempoTotalSemPeso / 10

tempoTotalComPeso = 0
for i in range(10):
    tempoTotalComPeso += tempoComPeso[i]

tempoMedioComPeso = tempoTotalComPeso / 10

# calculando as incertezas (incluindo operacao para ter apenas números positivos no somatório)
incertezaTempoSemPeso = 0

for i in range(10):
    incertezaTempoSemPeso += tempoMedioSemPeso - tempoSemPeso[i] if tempoMedioSemPeso > tempoSemPeso[i] else tempoSemPeso[i] - tempoMedioSemPeso
    
incertezaTempoSemPeso /= 10

incertezaTempoComPeso = 0

for i in range(10):
    incertezaTempoComPeso += tempoMedioComPeso - tempoComPeso[i] if tempoMedioComPeso > tempoComPeso[i] else tempoComPeso[i] - tempoMedioComPeso

incertezaTempoComPeso /= 10

print(f"Tempo médio sem peso e incerteza: ${tempoMedioSemPeso}  ${incertezaTempoSemPeso} \n")

print(f"Tempo médio com peso e incerteza: ${tempoMedioComPeso}  ${incertezaTempoComPeso} \n")