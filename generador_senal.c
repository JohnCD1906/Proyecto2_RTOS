#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

#define M   250    // No. de muestras de la senal
#define pi  3.14159265358979323846

int main(){

    FILE *file_senal;
    file_senal = fopen("x_n.dat", "w");

    srand(time(NULL));

    float A = 10.0 * rand()/RAND_MAX;    // Amplitud de la senal (+/- 5)
    float fo = 10.0 * rand()/RAND_MAX;   // No. ciclos en M muestras
    
    float x[M];

    for(int i=0; i<M; i++){
        x[i] = A*sin(2*pi*fo*i/M) + A*rand()/RAND_MAX;
        fprintf(file_senal, "%f\n", x[i]);
    }

    fclose(file_senal);

    system("gnuplot -p 'graficador.gp'");
    return 0;
}