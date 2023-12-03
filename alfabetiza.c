#include <stdlib.h>
#include <stdio.h>
int getStrLen(const char* string){
  int stringLength=0;
  while (string[stringLength]!='\0'){
    stringLength++;
  }
  return stringLength;
}
int numPlaces (int n) {
    int r = 1;
    while (n > 9) {
        n /= 10;
        r++;
    }
    return r;
}
char* shiftToTheRight(char* string){
  int stringLength=getStrLen(string)+1;
  for (int i=stringLength;i>0;i--){
    string[i]=string[i-1];
  }
  return string;
}
char* expandString(char* string){
    string=(char*)realloc(string,sizeof(char)*(getStrLen(string)+2));
    if (string==NULL){
      printf("Something terrible happened\n");
      return NULL;
    }
    string=shiftToTheRight(string);
    return string;
}
char *alphabet_position(const char *text) {
  printf("Text is: %s\n",text);
  int textLength=getStrLen(text);
  printf("Length is: %d\n",textLength);
  char* solution = (char*)malloc(sizeof(char));
  if (solution==NULL){
    printf("Something terrible happened\n");
    return NULL;
  }
  solution[0]='\0';
  for (int j=textLength-1;j>=0;j--){
    //printf("text[j] is: %d\n",text[j]);
    if ((text[j]>64 && text[j]<91)||(text[j]>96 && text[j]<123)){
      int alphaNumber=(int)text[j]-(text[j]<91 ? 64:96);
      for (int k=numPlaces(alphaNumber);k>0;k--){
        solution=expandString(solution);
        solution[0]=alphaNumber%10+'0';
        alphaNumber/=10;
      }
      if(j>0){
        solution=expandString(solution);
        solution[0]=' ';
      }
    }
  }
  return solution;
}
int main(){
  char* solution=alphabet_position("hola");
  printf("%s",solution);
  free(solution);
}
