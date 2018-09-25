#include <stdio.h>
#include <stdlib.h>

void main(void){
    int pass = 0;
    while(1){
        scanf("%d", &pass);
        if(pass == 2002){
            printf("Acesso Permitido\n");
            break;
        }else{
            printf("Senha Invalida\n");
        }
    }
    system("pause");
}