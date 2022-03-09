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

int
main()
{
  // ideia geral (podem modificar à vontade!):
  // leia a variável n
  int n, i;
  int vetor[100] = {0,1};
  scanf("%d", &n);
  for(i = 2; i <= n; i++){
    vetor[i] = vetor[i-1] + vetor [i-2];
    }
  //
  // imprima o n-ésimo elemento da série de fibonacci
  //
  printf("%d\n", vetor[n]);

  return 0;
}