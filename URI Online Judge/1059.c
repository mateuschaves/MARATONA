#include <stdio.h>
#include <stdlib.h>

void main(void){
    int i;
    for(i = 1; i <= 100; i++){
        if(i % 2 == 0)
            printf("%d\n", i );
    }
    system("pause");
}