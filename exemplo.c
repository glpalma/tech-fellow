#include <stdio.h>

int main() {
    double num_real;
    scanf("%lf", &num_real);

    int inteiro = num_real; // cast para inteiro

    if (inteiro % 2 == 0) {
        printf("Par\n");
    } else {
        printf("Impar\n");
    }

    return 0;
}