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

typedef struct real
{
  int parteInteira;
  int parteFracionaria;
} Real;

Real 
exercicio7a(Real a, Real b)
{
  Real c;
  c.parteInteira = a.parteInteira + b.parteInteira;
  c.parteFracionaria = a.parteFracionaria + b.parteFracionaria;
  if (c.parteFracionaria == 10){
    c.parteInteira += 1;
    c.parteFracionaria = 0;
  };

  return c;
}