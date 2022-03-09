// ===================================================
// Lista de Exercícios A1
// Curso de Programação II
// https://igormcoelho.github.io/curso-programacao-ii
// ===================================================
//
// Nome: xxxxxxxx
// Data:
//
// ===================================================

#include <stdio.h>
#include <string.h>
#include <stdlib.h>
 



int exercicio02(int k, int n){
    
  char valor_char = k + '0';
  char num[10];
  int i,cont = 0;
  sprintf(num, "%d", n);
  int tamanho = strlen(num);
  for(i = 0; i<tamanho; i++){
    if(num[0+i] != valor_char && num[0+i] != '0' && valor_char != '0'){
      num[0+i] = '0';
      int new_num = atoi(num);
      exercicio02(k,new_num); 
    }
    else if (valor_char == 0){
      num[0+i] = '1';
      int new_num = atoi(num);
      exercicio02(k,new_num);
    }
    else if(valor_char == num[0+i]){
      cont += 1;
    }
  }
  return cont;
};

int main(){
    int x = exercicio02(0, 762001092);
    printf("%d", x);
    return 0;

}