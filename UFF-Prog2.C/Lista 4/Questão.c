#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct tlista{
        int n;
        struct tlista *prox;
}tlista;
 
tlista *lu_insereinicio(tlista *plst, int pn)
{
       tlista *aux;
       aux = (tlista*)malloc(sizeof(tlista));
       aux -> n = pn;
       aux -> prox = plst;
       return aux;
}

void
ordenacao1(int v[], int N)
{
  int i, j, min, aux;
  for (i = 0; i < (N-1); i++) 
  {
     min = i;
     for (j = (i+1); j < N; j++) {
       if(v[j] < v[min]) 
         min = j;
     }
     if (i != min) {
       aux = v[i];
       v[i] = v[min];
       v[min] = aux;
     }
  }
}


void
ordenacao2(int v[], int min, int max)
{
  int pivo = min, i,ch,j;         
  for(i=min+1;i<=max;i++){        
   j = i;                      
   if(v[j] < v[pivo]){     
    ch = v[j];               
    while(j > pivo){           
     v[j] = v[j-1];      
     j--;                    
    }
    v[j] = ch;               
    pivo++;                    
   }
  }
  if(pivo-1 >= min){             
   ordenacao2(v,min,pivo-1);      
  }
  if(pivo+1 <= max){              
   ordenacao2(v,pivo+1,max);      
  }
 } 



int
main(int argc, char* argv[])
{
  char* arquivo;

  FILE* f = fopen("dados_101.txt", "r");

  int num, i; // ESTE É O NUMERO QUE SERÁ LIDO DO ARQUIVO E PASSADO PARA A LISTA
  tlista *list; // ESTOU CRIANDO A LISTA, NADA DE NOVO
  list = NULL;
  if(f){
    do{
      fscanf(f,"%d",&num);
      list = lu_insereinicio(list, num);
    }while(!feof(f));
  }
  
  
  int N, breaks, mediana, seq_min, seq_max;
  int parametros[5] = {&list[0], &list[1], &list[2], &list[3], &list[4]};
  int v1[parametros[4]];
  int v2[parametros[4]];
  for(i=0;i<parametros[4];i++){
    int i2 = 1;
    v1[i] = &list[parametros[4]-i2];
    i2++;
  }
  for(i=0;i<parametros[4];i++){
    v2[i] = v1[i];
  }
  fclose(f);

  // ====================
  // testa ordenação 1

  //
  ordenacao1(v1, parametros[4]);
  printf("MIN v1 = %d (esperado %d)\n", v1[0], parametros[1]);
  printf("MAX v1 = %d (esperado %d)\n", v1[parametros[4] - 1], parametros[0]);
  printf("MED v1 = %d (esperado %d)\n", v1[parametros[4] / 2], parametros[2]);
  

  // ====================
  // testa ordenação 2
  ordenacao2(v2, parametros[1], parametros[0]);
  printf("MIN v2 = %d (esperado %d)\n", v2[0], seq_min);
  printf("MAX v2 = %d (esperado %d)\n", v2[parametros[4] - 1], parametros[0]);
  printf("MED v2 = %d (esperado %d)\n", v2[parametros[4] / 2], parametros[2]);
  

  // ====================
  free(v1);
  free(v2);

  return 0;
}