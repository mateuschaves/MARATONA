#include <stdio.h>
#include <stdlib.h>

void main(void){
    int n, i, e;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%d", &e);
        if(e > 8000)
            printf("Mais de 8000!\n");
        else
            printf("Inseto!\n");
    }
    system("pause");
}