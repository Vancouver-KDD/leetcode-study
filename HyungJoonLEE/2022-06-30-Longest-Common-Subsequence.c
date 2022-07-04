#include "common.h"

int longestCommonSubsequence(char * text1, char * text2){
    int len_text1 = strlen(text1);
    int len_text2 = strlen(text2);

    int **arr;
    int i,j;
    arr = calloc(len_text1 + 1, sizeof(int*));

    for (i = 0; i < len_text1 + 1; i++) {
        arr[i] = calloc(len_text2 + 1, sizeof(int));
    }

    for (i = 1;i < len_text1 + 1; i++) {
        for (j = 1; j < len_text2 + 1; j++) {
            if (text1[i - 1] == text2[j - 1]) {
                arr[i][j] = arr[i - 1][j - 1] + 1;
            }else {
                if (arr[i - 1][j] > arr[i][j - 1]) arr[i][j] = arr[i-1][j];
                else arr[i][j] = arr[i][j-1];
            }
        }
    }

    return arr[len_text1][len_text2];
}



// TODO: Why this is not working?
//static int temp = 0;
//
//bool helper(char* text, char alpha) {
//    for (int i = temp; i < strlen(text); i++) {
//        if (text[i] == alpha) {
//            temp = i;
//            return true;
//        }
//    }
//    return false;
//}
//
//int longestCommonSubsequence(char * text1, char * text2){
//    int size = strlen(text2);
//    int count = 0;
//    for (int i = 0; i < size; i++) {
//        if (helper(text1, text2[i]) == true) count++;
//    }
//    return count;
//}



