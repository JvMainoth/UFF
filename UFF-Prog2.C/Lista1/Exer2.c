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

int
main()
{
  // ideia geral (podem modificar à vontade!):
  // leia o número c (onde, 33 <= c <= 126)
  int c, i, vf;
  vf = 0;
  scanf("%d\n", &c);
  char f = c;
  // leia a cadeia de caracteres/string s (com no máximo 50 elementos)
  char s[50];
  scanf("%s", s);
  for (i = 0; i <= 50; i++){
      if(s[i] == f){
          vf = 1;
      }

  } 




  //
  // converta o número c para um caractere, de acordo com tabela ASCII
  //
  // imprima: o tamanho da string e o número 1 ou 0, onde 1 indica que o caractere c existe na string s; 0 caso contrário
  //
  printf("%d %d\n",strlen(s), vf);


  return 0;
}