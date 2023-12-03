#include <stdio.h>
#include <stddef.h>
#include <stdlib.h>
int binLength=0;
char* numToBinary(unsigned num){
  binLength=0;
  char* binary=(char*)malloc(sizeof(char));
  if (binary==NULL){
    printf("Something terrible happened\n");
    return NULL;
  }
  if (num==0){
    binary[0]='0';
    binLength=1;
    return binary;
  }
  while (num>0){
    binLength++;
    if (binLength>1){
      binary=(char*)realloc(binary, binLength*sizeof(char));
      if (binary==NULL){
        printf("Something terrible happened\n");
        return NULL;
      }
      for (int j=binLength-1;j>0;j--){
        binary[j] = binary[j-1];
      }
    }
    binary[0] = '0'+num%2;
    num/=2;
  }
  return binary;
}
size_t countBits(unsigned value) {
  printf("The value is %u\n",value);
  char* binary = numToBinary(value);
  size_t count = 0;
  printf("Array length is %d\n",binLength);
  printf("Binary is ");
  for (int i=0;i<binLength;i++){
    printf("%c",binary[i]);
    if (binary[i]=='1'){
      count++;
    }
  }
  printf("\n");
  printf("The count is %zu\n",count);
  free(binary);
  return count;
}
int main(){
  unsigned num;
  printf("Enter an integer to count the number of 1s in its binary representation (smaller than 2^32): ");
  scanf("%d",&num);
  countBits(num);
  return 0;
}