// Curso de Programação II
// https://igormcoelho.github.io/curso-programacao-ii
// ===================================================
//
// Nome: xxxxxxxx
// Data:
//
// ===================================================

#include <stdio.h>

int
main()
{
  // ideia geral (podem modificar à vontade!):
  // leia a variável N
  int N, i, r1, r2, q1, q2;
  int vetor[100];
  scanf("%d", &N);
  for(i = 0; i < N; i++){
      scanf ("%d", &vetor[i]);
    }
  r1 = vetor[1] - vetor[0];
  r2 = vetor[2] - vetor[1];
  q1 = vetor[1] / vetor[0];
  q2 = vetor[2] / vetor[1];
  if (r1 == r2){
    printf("PA");
  }
  else if(q1 == q2){
    printf("PG");
  }
  else{
    printf("NA\n");
  } 
  //
  // considerem os próximos N números (através da Entrada Padrão) e
  // indiquem (através da Saída Padrão) se é PA, PG ou NA (nenhum dos dois).
  //


  return 0;
}