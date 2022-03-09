#include <stdio.h>

typedef struct real
{
  int parteInteira;
  int parteFracionaria;
} Real;

// 7. Suponha que um número real é representado como o 'struct real' acima
//
// c) Escreva uma função que imprima um número real 'a' com vírgula ao invés de ponto.
void
exercicio7c(Real a, char saida[])
{
  char resultado[] = "0,0";
  sprintf(resultado[0],"%d", a.parteInteira);
  sprintf(resultado[2],"%d", a.parteFracionaria);
  strcpy(saida, resultado);
}