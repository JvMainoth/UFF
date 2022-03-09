
#include <stdio.h>
#include <string.h>
#include <stdlib.h>

typedef struct lista{
        int iNum;
        struct lista *pLista;
}lista;


lista *lu_insereinicio(lista *pLista, int iNum)
{
       lista *pAux = NULL;
       pAux = (lista*)malloc(sizeof(lista));
       pAux -> iNum = iNum;
       pAux -> pLista = pLista;
       return pAux;
}

int getTamanhoLista(lista *pLista) {
    int iTam = 0;
    lista *pAux = pLista;
    while (pAux != NULL) {
          iTam++;
          pAux = pAux->pLista;
    }
    return iTam;
} 

void criaVetor(lista *pLista, int *pVet) {
     int iTamLista = 0;
     int i = 0;
     lista *pAux = pLista;
      
     iTamLista = getTamanhoLista(pLista);
     pVet = (int *) malloc(sizeof(int) * iTamLista);
      
      
     while (pAux != NULL) {
           pVet[i] = pAux->iNum;
           pAux = pAux->pLista;
           i++;
     }
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
  lista *list; // ESTOU CRIANDO A LISTA, NADA DE NOVO
  list = NULL;
  int*pVet = NULL;
  if(f){
    do{
      fscanf(f,"%d",&num);
      list = lu_insereinicio(list, num);
    }while(!feof(f));
  }
  criaVetor(list,pVet);
  
  

  return 0;
}