#include <stdio.h>
#include <stdlib.h>

void fun (int ** values){
   printf("SIckcunt\n");

}

int main(){

   int numbers1[5][4];

   int * numbers2 = malloc (5*4*sizeof(int));


   int ** numbers3 = malloc (5 * sizeof(int *)); 
   for (int r = 0; r < 5; r++) {
      numbers3[r] = malloc(4 * sizeof(int));
   }

   printf("%lu %lu %lu\n", sizeof(numbers1), sizeof(numbers2), sizeof(numbers3));
   fun(numbers1);
   fun(numbers2);
   fun(numbers3);

   free(numbers2);
   free(numbers3);
}
