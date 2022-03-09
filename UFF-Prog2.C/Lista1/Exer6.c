#include <stdio.h>

int
main()
{
  // ideia geral (podem modificar à vontade!):
  // leia a variável N
  int N, i;
  float soma, resultado, div, num;
  float vetor[100];
  div = 10;
  num = 1;  
  scanf("%d", &N);
  for(i = 0; i < N; i++){
        resultado = num/div;
        vetor[i] = resultado;
        div = div + 5;
        num ++;
        soma = soma + vetor[i];
    }
  // apresente a soma dos N primeiros termos da seguinte sequência:
  // 1/10 + 2/15 + 3/20 + 4/25 + ...
  // imprima o resultado com duas casas decimais
  printf("%.2f\n", soma);

  return 0;
}