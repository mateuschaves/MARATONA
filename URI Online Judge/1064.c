#include <stdio.h>
#include <stdlib.h>

void main(void){
    float s, n = 0;
    int p = 0;
    int i;
    for(i = 0; i < 6; i++){
        scanf("%f", &n);
        if(n > 0){
            p++;
            s = s + n;
        }
    }
    printf("%d valores positivos\n", p);
    printf("%.1f\n", s / (float) p);
    system("pause");
}