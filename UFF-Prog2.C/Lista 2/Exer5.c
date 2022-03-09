#include <stdio.h>

typedef struct real
{
  int parteInteira;
  int parteFracionaria;
} Real;

// 7. Suponha que um número real é representado como o 'struct real' acima
//
// d) Escreva uma função que converta um número 'a' do tipo real para um número do tipo float.
float
exercicio7d(Real a)
{
  float c;
  c = a.parteFracionaria / 10;
  c += a.parteInteira;
  return c;
}