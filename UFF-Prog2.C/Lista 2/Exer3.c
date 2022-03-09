#include <stdio.h>

typedef struct real
{
  int parteInteira;
  int parteFracionaria;
} Real;


Real
exercicio7b(Real a, int i)
{
  Real c;
  c.parteInteira = a.parteInteira + i;
  c.parteFracionaria = a.parteFracionaria;
  return c;
}