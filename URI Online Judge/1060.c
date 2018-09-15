#include <stdio.h>
#include <stdlib.h>


int isPositive(int n);

void main(void){
    int p, i;
    float n;
    for(i = 0; i < 6; i++){
        scanf("%f", &n);
        if(isPositive(n) == 1){
            p++;
        }
    }
    printf("%d valores positivos\n", p);
    system("pause");
}

int isPositive(int n){
    if (n > 0){
        return 1;
    }else{
        return 0;
    }
}