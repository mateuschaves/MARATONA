#include <stdio.h>
#include <stdlib.h>

void main(void){
    int i, q, n;
    q = 0;
    for(i = 0; i < 5; i++){
        scanf("%d", &n);
        if(n % 2 == 0)
            q++;
    }
    printf("%d valores pares\n", q);
    system("pause");
}