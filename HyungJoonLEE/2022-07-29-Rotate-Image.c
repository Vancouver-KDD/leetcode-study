#include "common.h"

void rotate(int** matrix, int matrixSize, int* matrixColSize){
    for(int i = 0; i < matrixSize / 2; i++){
        for(int j = i; j < matrixSize - i - 1; j++){
            int a = matrix[i][j];
            int b = matrix[j][matrixSize - i - 1];
            int c = matrix[matrixSize - i - 1][matrixSize -j -1];
            int d = matrix[matrixSize - j - 1][i];
            matrix[i][j] = d;
            matrix[j][matrixSize - i -1] = a;
            matrix[matrixSize - 1 - i][matrixSize - 1 - j] = b;
            matrix[matrixSize - 1 - j][i] = c;
        }
    }
}
