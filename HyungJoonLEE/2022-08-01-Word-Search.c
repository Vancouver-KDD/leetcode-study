#include "common.h"



bool DFS(char** board, int boardSize, int* boardColSize, char* word, int len, int index, int i, int j, bool** visited) {
    if (index == len ) return true;
    if ( i < 0 || j < 0 || i >= boardSize || j >= *boardColSize || visited[i][j] || board[i][j] != word[index]) return false;
    visited[i][j] = 1;
    bool ans =  DFS(board, boardSize, boardColSize, word, len, index+1, i+1, j, visited) ||
                DFS(board, boardSize, boardColSize, word, len, index+1, i-1, j, visited) ||
                DFS(board, boardSize, boardColSize, word, len, index+1, i, j+1, visited) ||
                DFS(board, boardSize, boardColSize, word, len, index+1, i, j-1, visited);
    visited[i][j] = 0;
    return ans;
}



bool exist(char** board, int boardSize, int* boardColSize, char * word) {
    int len = strlen(word);
    bool** visited = malloc(sizeof(bool*)*boardSize);
    for (int i = 0; i < boardSize; i++){
        visited[i] = malloc(sizeof(bool) * (*boardColSize));
        memset(visited[i], 0, *boardColSize);
    }

    for (int i = 0; i < boardSize; i++){
        for (int j = 0 ; j < *boardColSize; j++){
            if (DFS(board, boardSize, boardColSize, word, len, 0, i, j, visited)) return true;
        }
    }
    return false;
}