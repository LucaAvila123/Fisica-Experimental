#include <stdio.h>

void calculaTempos(float* arrayDeTempo, float tempoMedio, float incertezaTempo, float tempoMedioQuadrado, float incertezaTempoQuadrado);
int main(){

    float tempoSemPesoFinal[10] = {2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490};
    float tempoComPesoFinal[10] = {2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205};
    float arrayValoresCalculadosSemPesoFinal[4] = {0, 0, 0, 0};
    float arrayValoresCalculadosComPesoFinal[4] = {0, 0, 0, 0};
    
    calculaTempos(tempoSemPesoFinal, arrayValoresCalculadosSemPesoFinal[0], arrayValoresCalculadosSemPesoFinal[1], arrayValoresCalculadosSemPesoFinal[2], arrayValoresCalculadosSemPesoFinal[3]);
    calculaTempos(tempoComPesoFinal, arrayValoresCalculadosComPesoFinal[0], arrayValoresCalculadosComPesoFinal[1], arrayValoresCalculadosComPesoFinal[2], arrayValoresCalculadosComPesoFinal[3]);
 
    printf("Tempo médio sem peso e incerteza: %.2f %.2f\n", arrayValoresCalculadosSemPesoFinal[0], arrayValoresCalculadosSemPesoFinal[1]);
    printf("Tempo médio sem peso ao quadrado e incerteza: %.2f %.2f\n", arrayValoresCalculadosSemPesoFinal[2], arrayValoresCalculadosSemPesoFinal[3]);
    printf("Tempo médio com peso e incerteza: %.2f %.2f\n", arrayValoresCalculadosComPesoFinal[0], arrayValoresCalculadosComPesoFinal[1]);
    printf("Tempo médio com peso ao quadrado e incerteza: %.2f %.2f\n", arrayValoresCalculadosComPesoFinal[2], arrayValoresCalculadosComPesoFinal[3]);
    return 0;
}

void calculaTempos(float* arrayDeTempo, float tempoMedio, float incertezaTempo, float tempoMedioQuadrado, float incertezaTempoQuadrado){
    // calculando tempo médio
    float tempoTotal = 0;
    float tempoTotalQuadrado = 0;

    for(int i = 0; i < 10; i++){
        tempoTotal += arrayDeTempo[i];
        tempoTotalQuadrado += arrayDeTempo[i]*arrayDeTempo[i];
    }
    tempoMedio = tempoTotal / 10;
    tempoMedioQuadrado = tempoTotalQuadrado / 10;


    // calculando as incertezas (incluindo operacao para ter apenas números positivos no somatório)
    incertezaTempo = 0;
    incertezaTempoQuadrado = 0;
    
    for(int i = 0; i < 10; i++){
        incertezaTempo += tempoMedio > arrayDeTempo[i] ? tempoMedio - arrayDeTempo[i] : arrayDeTempo[i] - tempoMedio;
        incertezaTempoQuadrado += tempoMedioQuadrado > arrayDeTempo[i]*arrayDeTempo[i] ? tempoMedioQuadrado - arrayDeTempo[i]*arrayDeTempo[i] : arrayDeTempo[i]*arrayDeTempo[i] - tempoMedioQuadrado;
    } 
    incertezaTempo /= 10;
    incertezaTempoQuadrado /= 10;
}