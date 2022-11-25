#include <stdio.h>

void calculaTempos(float* arrayDeTempo, int opcao);
int main(){

    float tempoSemPesoFinal[10] = {2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490};
    float tempoComPesoFinal[10] = {2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205};

    printf("Tempo médio sem peso final e incerteza: ");
    calculaTempos(tempoSemPesoFinal, 1);
    printf("Tempo médio ao quadrado sem peso e incerteza: ");
    calculaTempos(tempoSemPesoFinal, 2);

    printf("Tempo médio com peso e incerteza: ");
    calculaTempos(tempoComPesoFinal, 1);
    printf("Tempo médio ao quadrado com peso e incerteza: ");
    calculaTempos(tempoComPesoFinal, 2);

    
}

void calculaTempos(float* arrayDeTempo, int opcao){
    // calculando tempo médio
    float tempoTotal = 0;
    float tempoTotalQuadrado = 0;
    float tempoMedio = 0;
    float tempoMedioQuadrado = 0;
    float incertezaTempo = 0;
    float incertezaTempoQuadrado = 0;

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
    
    // deixei opcao como expoente do número que está sendo procurado
    if(opcao == 1){
        printf("%f %f\n", tempoMedio, incertezaTempo);
    }

    else if(opcao == 2){
        printf("%f %f\n", tempoMedioQuadrado, incertezaTempoQuadrado);
    }
    
}