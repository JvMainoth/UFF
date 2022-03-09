#include<stdio.h>
int soma(int a, int b){
    int resultado;
    resultado = a + b;
    return (resultado);

}

int sub(int a, int b){
    int resultado;
    resultado = a - b;
    return (resultado);

}

int mult(int a, int b, int *r){
    *r = a * b;
}

int div(int a, int b, int *r){
    *r = a / b;
}

int main () {
  int a, b, c;
  scanf("%d %d",&a, &b);
  c = soma(a,b);
  printf("Soma: %d\n", c);
  c = sub(a,b);
  printf("Subtração: %d\n", c);
  mult(a,b,&c);
  printf("Multiplicação: %d\n", c);
  div(a,b,&c);
  printf("Divisão: %d\n", c);
  return 0;
}
