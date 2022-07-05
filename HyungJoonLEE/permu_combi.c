#include "common.h"

int *arr;
void swap(int *a, int *b);
void print_arr(int c);
void permutation(int n, int r, int depth);

void swap(int *a, int *b){ //값을 변환해주는 함수
    int tmp;
    tmp = *a;
    *a = *b;
    *b = tmp;
}

void print_arr(int c){//배열을 프린트해주는 함수
    for(int i = 0; i < c; i++){
        printf("%d ", arr[i]);
    }
    printf("\n");
}

void permutation(int n, int r, int depth){
    if (r == depth){
        print_arr(depth);
        return;
    }
    for (int i = depth; i < n; i++) {
        swap(&arr[i], &arr[depth]);
        permutation(n, r,depth + 1);
        swap(&arr[i], &arr[depth]);
    }
}

int main(){
    int n, r;

    //n과 r을 공백을 두고 입력
    printf("(숫자) (숫자)를 입력:\n");
    scanf("%d %d", &n, &r);

    //n개의 배열 할당 후 값 삽입
    arr = (int*)malloc(n * sizeof(int));
    for(int i = 0; i < n; i++) {
        arr[i] = i + 1;
    }

    permutation(n, r, 0);
    free(arr); //동적 할당 해제
    return 0;
}
