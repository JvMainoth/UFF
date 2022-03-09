#include <stdio.h>

// 1. Faça uma função recursiva que recebe como parâmetros um vetor de inteiros,
// a posição inicial do vetor e a posição final do vetor,
// e inverte a posição dos elementos do vetor
//
void exercicio01(int v[], int primeiro, int ultimo) {
  int temp = v[primeiro];
  int ulttemp = ultimo - primeiro;
  v[primeiro] = v[ulttemp];
  v[ulttemp] = temp;
  if (ultimo % 2 == 1 && primeiro < (ultimo-1)/2){
    exercicio01(v, primeiro+1, ultimo);
  }
  else if (primeiro < ultimo/2-1){
    exercicio01(v, primeiro+1, ultimo);
  
}
}

int main() {
   int vetor[8] = {80,70,60,50,40,30,20,10};
   int primeiro = 0;
   int ultimo = 7;
   int i;
   exercicio01(vetor, primeiro, ultimo);
   for(i = 0; i<= ultimo; i++){
       printf("notas[%d] = %d\n", i, vetor[i]);
   }
   
   return 0;

}