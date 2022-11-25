#include <stdio.h>

void calculaTempos(float* arrayDeTempo, FILE* saida, int opcao);
int main(){
    float tempoSemPeso1[10] = {1.01880, 1.04305, 1.04175, 1.01260, 1.05720, 1.03265, 1.05005, 1.03700, 1.04290, 1.02375};
    float tempoComPeso1[10] = {1.21060, 1.20395, 1.22555, 1.21305, 1.22165, 1.22450, 1.21265, 1.21865, 1.23740, 1.21260};
    
    float tempoSemPeso2[10] = {1.48490, 1.51075, 1.50865, 1.47620, 1.52875, 1.49615, 1.51485, 1.50420, 1.51070, 1.49340};
    float tempoComPeso2[10] = {1.75520, 1.74525, 1.76630, 1.75585, 1.76790, 1.76765, 1.75775, 1.76305, 1.78355, 1.75030};

    float tempoSemPeso3[10] = {1.84680, 1.87090, 1.86890, 1.83580, 1.89230, 1.85650, 1.87435, 1.86730, 1.87315, 1.85730};
    float tempoComPeso3[10] = {2.17555, 2.16515, 2.18655, 2.17575, 2.18955, 2.18900, 2.18040, 2.18400, 2.20635, 2.16935};

    float tempoSemPesoFinal[10] = {2.14280, 2.16565, 2.16330, 2.12995, 2.18985, 2.15090, 2.16955, 2.16385, 2.16675, 2.15490};
    float tempoComPesoFinal[10] = {2.51920, 2.50820, 2.52930, 2.51900, 2.53460, 2.53390, 2.52630, 2.52860, 2.55195, 2.51205};
    FILE* saida = fopen("saidaFisicaExperimental", "w");
    
    fprintf(saida, "Primeiro\n");
    fprintf(saida, "Sem peso\n");
    calculaTempos(tempoSemPeso1, saida, 1);

    fprintf(saida, "\nCom peso\n");
    calculaTempos(tempoComPeso1, saida, 1);
    fprintf(saida, "\nSegundo\n");
    fprintf(saida, "Sem peso\n");
    calculaTempos(tempoSemPeso2, saida, 1);

    fprintf(saida, "\nCom peso\n");
    calculaTempos(tempoComPeso2, saida, 1);
    
    fprintf(saida, "\nTerceiro\n");
    fprintf(saida, "Sem peso\n");
    calculaTempos(tempoSemPeso3, saida, 1);

    fprintf(saida, "\nCom peso\n");
    calculaTempos(tempoComPeso3, saida, 1);
    
    fprintf(saida, "\nFinal\n");
    fprintf(saida, "Sem peso\n");
    calculaTempos(tempoSemPesoFinal, saida, 1);

    fprintf(saida, "\nCom peso\n");
    calculaTempos(tempoComPesoFinal, saida, 1);

    fclose(saida);
    FILE* tabela3 = fopen("tabela3", "w");
    fprintf(tabela3, "    primeiro    |   segundo   |   terceiro  |  quarto\n");
    fprintf(tabela3, "m2a");
    fclose(tabela3);
}

void calculaTempos(float* arrayDeTempo, FILE* saida, int opcao){
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
    if(opcao == 1){
        fprintf(saida, "Tempo médio e incerteza: %f ± %f\n", tempoMedio, incertezaTempo);
        fprintf(saida, "Tempo médio ao quadrado e incerteza: %f ± %f\n", tempoMedioQuadrado, incertezaTempoQuadrado);
    }

}