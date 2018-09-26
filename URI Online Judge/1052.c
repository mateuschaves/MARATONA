#include <stdio.h>
#include <stdlib.h>

void main(void){
    int n;
    scanf("%d", &n);
    enum days{january = 1, february, march, april, may, june, july, august, september, october, november, december};
    switch (n)
    {
        case january:
            printf("January\n");
            break;
        case february:
            printf("February\n");
            break;
        case march:
            printf("March\n");
            break;
        case april:
            printf("April\n");
            break;
        case may:
            printf("May\n");
            break;
        case june:
            printf("June\n");
            break;
        case july:
            printf("July\n");
            break;
        case august:
            printf("August\n");
            break;
        case october:
            printf("October\n");
            break;
        case november:
            printf("November\n");
            break;
        case september:
            printf("September\n");
            break;
        case december:
            printf("December\n");
            break;
    }
    system("pause");
}