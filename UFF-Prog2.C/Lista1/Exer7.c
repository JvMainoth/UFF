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
  float num, soma, media;
  int i;
  float vetor[100];
  i = 0;
  while (num > 0){
        scanf ("%d", &num);
        vetor[i] = num;
        soma = soma + num;
        i++;
    }
    media = soma/i+1;
  // ideia geral (podem modificar à vontade!)

  printf("%.2f", media);

  return 0;
}