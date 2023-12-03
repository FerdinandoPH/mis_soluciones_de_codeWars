#include <stdio.h>
#include <stdlib.h>
#include <inttypes.h>
uint64_t getListLength(uint64_t n){ //gets how many digits the number has
  uint64_t length=1; 
  while (n>=10){ 
    length++;
    n/=10;
  }
  return length;
}
uint64_t isOrdered(uint64_t* arr, uint64_t length){
  for (int i=0;i<length-1;i++){
    if (arr[i]<arr[i+1]){
      return 0;
    }
  }
  return 1;
}
uint64_t descendingOrder(uint64_t n) {
    uint64_t solution = 0;
    uint64_t length = getListLength(n);
    uint64_t* arr = (uint64_t*)malloc(length * sizeof(uint64_t));
    if (arr == NULL) {
        printf("Something terrible happened\n");
        return -1;
    }
    for (int i = 0; i < length; i++) {
        arr[i] = n % 10;
        n = n / 10;
    }

    while (isOrdered(arr, length) == 0) {
        for (int i = 0; i < length - 1; i++) {
            if (arr[i] < arr[i + 1]) {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
            }
        }
    }
    for (int i = 0; i < length; i++) {
        solution = solution * 10ULL + arr[i];
    }

    free(arr);
    return solution;
}
// uint64_t descendingOrder(uint64_t n)
// {
//   // I know this method is overcomplicated, but I wanted to learn how to use dynamic arrays and malloc
//   uuint64_t solution=0;
//   uint64_t length = getListLength(n);
//   printf("%d\n",length);
//   uint64_t* arr = (uint64_t*)malloc(length*sizeof(uint64_t)); //Creates a dynamic array to store the digits and sort them
//   if (arr==NULL){
//     printf("Something terrible happened\n");
//     return -1;
//   }
//   printf("here\n");
//   for (int i=0;i<length;i++){
//     arr[i]=n%10;
//     printf("Saved as %d\n",arr[i]);
//     n=n/10;
//   }
//   while (isOrdered(arr,length)==0){ //sorts the digits
//     for (int i=0;i<length-1;i++){
//       if (arr[i]<arr[i+1]){
//         int temp = arr[i];
//         arr[i]=arr[i+1];
//         arr[i+1]=temp;
//       }
//     }
//     printf("State of the list: ");
//     for (int i=0;i<length;i++){
//       printf("%d",arr[i]);
//     }
//     printf("\n");
//   }
//   printf("Final state of the list: ");
//   for (int i=0;i<length;i++){
//     printf("%d",arr[i]);
//   }
//   printf("\n");
//   for (int i=0;i<length;i++){ //puts the solution back into a number
//     printf("Now solution is %lld*10+%d=",solution,arr[i]);
//     solution=solution*10ULL+(uint64_t)arr[i];
//     printf("%d\n",solution);
//   }
//   free(arr);
//   return solution;
// }
int main(){
  printf("%lld\n",descendingOrder(1469594179));
  return 0;
}