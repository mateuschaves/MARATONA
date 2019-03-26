#include <stdio.h>
#include <math.h>

int main(void) {
  int q, i, n, k;
  scanf("%d", &q);
  for(i = 0; i < q; i++){
	  scanf("%d", &n);
	  for(k = 2;  k <= floor(sqrt(n)); k++){
		  if(n % k == 0){
			printf("Not Prime\n");
			k = -1;
			break;
		  }
	  }
	  if(k != -1){
	  	printf("Prime\n");
	  }
  }
}
