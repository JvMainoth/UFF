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
  // leia números n1 e n2
  int n1, n2, n3, d, r, rr;
  scanf("%d %d", &n1, &n2);
  if (n1 < n2){
    n3 = n1;
    n1 = n2;
    n2 = n3;
  }
  r = n1 % n2;
  d = n2;
  while (r > 1){
      rr = r;
      r = d % r;
      d = rr;
    }
  if (r == 0){
      printf("0\n");
  }
  else{
      printf("1\n");
  }

  //
  // imprima 1 se forem coprimos, 0 caso contrário
  //


  return 0;
}