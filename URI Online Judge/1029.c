#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n, int *c);

void main(void){
    int n, b, l;
    scanf("%d", &n);
    for(l = 0; l < n; l++){
        int *c = malloc(sizeof(int));
        *c = -1;
        scanf("%d", &b);
        int i = fibonacci(b, c);
        printf("fib(%d) = %d calls = %d\n", b, *c, i);
    }
    system("pause");
}

int fibonacci(int n, int *c){
    *c = *c + 1;
    if (n == 0){
        return 0;
    }else if(n == 1){
        return 1;
    }else {
        return fibonacci(n - 1, c) + fibonacci(n - 2, c);
    }
}