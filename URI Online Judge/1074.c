#include <stdio.h>
#include <stdlib.h>

void main(void){
    int n, i, a;
    scanf("%d", &n);
    for(i = 0; i < n; i++){
        scanf("%d", &a);
        if(a == 0){
            printf("NULL\n");
        }else if( a  % 2 == 0){
            printf("EVEN ");
        }else{
            printf("ODD ");
        }
        if(a > 0){
            printf("POSITIVE\n");
        }else if(a != 0){
            printf("NEGATIVE\n");
        }
    }
    system("pause");
}