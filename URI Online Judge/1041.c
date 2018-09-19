#include <stdio.h>
#include <stdlib.h>

void main(void){
    float x, y;
    scanf("%f%f", &x, &y);
    if(x == 0 && y == 0){
        printf("Origem\n");
        system("pause");
        exit(0);
    }

    if(x == 0){
        printf("Eixo Y\n");
        system("pause");
        exit(0);
    }else if (y == 0){
        printf("Eixo X\n");
        system("pause");
        exit(0);
    }

    if(x > 0 && y > 0){
        printf("Q1\n");
    }else if(x < 0 && y > 0){
        printf("Q2\n");
    }else if(x < 0 && y < 0){
        printf("Q3\n");
    }else if(x > 0 && y < 0){
        printf("Q4\n");
    }
    system("pause");
}