#include <stdio.h>
#include <stdlib.h>

void main(void){
    int a, b, s, i = 0;
    scanf("%d%d", &a, &b);
    if(a > b){
        for(i = b; i < a; i++){
            if(i % 2 != 0){
                if(i < 0)
                    i *= -1;
                s += i;
            }
        }
    }else{
        for(i = a; i <= b; i++){
            if(i % 2 != 0){
                if(i < 0)
                    i *= -1;
                s += i;
            }
        }
    }
    printf("%i\n", s);
    system("pause");
}