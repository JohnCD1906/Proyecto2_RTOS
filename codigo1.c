//Primer código en C
#include <stdio.h>
#include <stdlib.h>
#include <wiringPi.h>

// Pines GPIO (numeracion BCM)
#define LED0 17   // bit 0 (LSB)
#define LED1 18   // bit 1
#define LED2 27   // bit 2
#define LED3 22   // bit 3 (MSB)

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

int main(int argc, char *argv[]) {
    if (argc < 2) {
        printf("Uso: %s [subir|bajar]\n", argv[0]);
        printf("  subir -> cuenta de 0x0 a 0xF\n");
        printf("  bajar -> cuenta de 0xF a 0x0\n");
        return 1;
    }

    setup_pines();

    if (strcmp(argv[1], "subir") == 0) {
        printf("Conteo: 0x0 -> 0xF\n");
        for (int i = 0x0; i <= 0xF; i++) {
            printf("  Valor: 0x%X\n", i);
            mostrar_valor(i);
            delay(300);  // 300ms entre cada valor
        }
    }
    else if (strcmp(argv[1], "bajar") == 0) {
        printf("Conteo: 0xF -> 0x0\n");
        for (int i = 0xF; i >= 0x0; i--) {
            printf("  Valor: 0x%X\n", i);
            mostrar_valor(i);
            delay(300);
        }
    }
    else {
        printf("Argumento invalido. Usa 'subir' o 'bajar'\n");
        apagar_leds();
        return 1;
    }

    apagar_leds();
    printf("Secuencia terminada.\n");
    return 0;
}