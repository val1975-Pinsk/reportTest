#include <stdio.h>
#include <string.h>
#include "report.h"

char strBuff[ 256 ];
char * p_b;
char * fileName = "Водители.html";

typedef struct{
  char name[ 100 ];
  int noCash;
}passData;

int main(){
  passData passenger = {"", no};
  char * p_pN = passenger.name;
  int sizeOfPassName = sizeof(passenger.name);
  printf("Opening file: %s\n", fileName);
  FILE * p_f = fopen ( fileName, "r" );
  if ( p_f == NULL ) {
    printf ( "Ошибка открытия файла. :(\n" );
  } else {
    printf ( "Файл открыт... Начинаю работу :)\n");
    while ((fgets(strBuff, 256, p_f)) != NULL){
      p_b = strBuff;
      if(strIsName(p_b)){
	clearPassengerName(p_pN, sizeOfPassName);
	writePassName(p_b, passenger.name);
       	printf("%s\n", passenger.name);
	continue;
      }
      /*if(strIsPayment(p_b)){
	if(isNoCash(p_b)){
	  passenger.noCash = yes;
	}
      }
      if(passenger.noCash){
	printf("Passenger name: %s\n", passenger.name);
	printf("noCash: %d\n", passenger.noCash);
	passenger.noCash = no;
	}*/
    }
  }
  return 1;
}
