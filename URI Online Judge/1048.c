#include <stdio.h>
#include <stdlib.h>

void main(void){
    float s, r;
    int p;
    scanf("%f", &s);
    if(s >= 0 &&  s <= 400){
        r = 0.15;
    }else if(s > 400 && s <= 800){
        r = 0.12;
    }else if(s > 800 && s <= 1200){
        r = 0.10;
    }else if(s > 1200 && s <= 2000){
        r = 0.07;
    }else{
        r = 0.04;
    }
    p = (int) r*100;
    printf("Novo salario: %0.2f\n", s*r + s);
    printf("Reajuste ganho: %0.2f\n", s*r);
    printf("Em percentual: %0.f %%\n", r*100);
    system("pause");
}