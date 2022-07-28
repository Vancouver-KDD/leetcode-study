#include "common.h"

void setZeroes(int** matrix, int matrixSize, int* matrixColSize){
    bool clr_first_col = false;
    bool clr_first_row = false;

    // Check whether first row needs to be cleared
    for(int i = 0; i < matrixSize; i++) {
        if(matrix[i][0] == 0) {
            clr_first_col = true;
            break;
        }
    }

    // Check whether first column needs to be cleared
    for(int j = 0;j < *matrixColSize; j++){
        if(matrix[0][j] == 0) {
            clr_first_row = true;
            break;
        }
    }

    // Check the inside matrix. Set element in first column and first row to zero to mark row and col to be cleared.
    for(int i = 1; i < matrixSize; i++) {
        for (int j = 1; j < *matrixColSize; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;
                matrix[0][j] = 0;
            }
        }
    }

    // Clear rest of the row and column in inside matrix if element is first row or first column is cleared
    for(int i = 1; i < matrixSize; i++) {
        for (int j = 1; j < *matrixColSize; j++) {
            if (matrix[0][j] == 0 || matrix[i][0] == 0) {
                matrix[i][j] = 0;
            }
        }
    }

    // Finally clear the first row and first column if needed
    if(clr_first_col) {
        for (int i = 0; i < matrixSize; i++) {
            matrix[i][0] = 0;
        }
    }

    if(clr_first_row) {
        for (int j = 0; j < *matrixColSize; j++) {
            matrix[0][j] = 0;
        }
    }
}