//Primer código en C
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <wiringPi.h>

// Pines GPIO (numeracion BCM)
#define LED0 17   // bit 0 (LSB)
#define LED1 18   // bit 1
#define LED2 27   // bit 2
#define LED3 23   // bit 3 (MSB)

int pines[4] = {LED0, LED1, LED2, LED3};

void setup_pines() {
    wiringPiSetupGpio();  // usar numeracion BCM
    for (int i = 0; i < 4; i++) {
        pinMode(pines[i], OUTPUT);
        digitalWrite(pines[i], LOW);
    }
}

void mostrar_valor(int valor) {
    // Escribe cada bit del valor en su LED correspondiente
    for (int i = 0; i < 4; i++) {
        digitalWrite(pines[i], (valor >> i) & 1);
    }
}

void apagar_leds() {
    for (int i = 0; i < 4; i++) {
        digitalWrite(pines[i], LOW);
    }
}

int main() {

    setup_pines();

        printf("Conteo: 0x0 -> 0xF\n");
        for (int i = 0x0; i <= 0xF; i++) {
            printf("  Valor: 0x%X\n", i);
            mostrar_valor(i);
            delay(500);  // 500ms entre cada valor
        }


    apagar_leds();
    printf("Secuencia terminada.\n");
    return 0;
}