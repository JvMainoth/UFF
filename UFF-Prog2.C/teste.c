#include <stdio.h>
#include <string.h>
#include <stdlib.h>

void insertion_sort(int *a,int tam)
{
 int i, j, tmp;//inicia contador
  
 for(i = 1; i < tam; i++){//começa um loop referente ao valor a frente do primeiro do vetor
    tmp = a[i];//armazena em um temporario
    for(j = i-1; j >= 0 && tmp < a[j]; j--){//entra nesse loop para locomover o valor do temp enquanto comparar com os valores anteriores do vetor
      a[j+1] = a[j];//se a situação for satisfeita a posição a frente vai receber o valor da posição atras
    }
    a[j+1] = tmp;// e joga o maior valor no temp para a posição
 }
}




int main(){
  int vet[5] = {5,1,4,2,4};
  int tam = 5;
  insertion_sort(vet, tam);
  printf("\n");
  return 0;
}

