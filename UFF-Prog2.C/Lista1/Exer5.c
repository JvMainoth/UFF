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
  // leia a variável N
  int N, i, soma;
  scanf("%d", &N);
  int vetor[100];
  soma = 0;
  for(i = 0; i < N; i++){
        scanf ("%d", &vetor[i]);
        if (vetor[i] % 2 == 0){
            soma = soma + vetor[i];
        }
    }
  //
  // considerem os próximos N números (através da Entrada Padrão) e
  // apresente a soma dos elementos que forem pares.
  //
  printf("%d\n", soma);

  return 0;
}