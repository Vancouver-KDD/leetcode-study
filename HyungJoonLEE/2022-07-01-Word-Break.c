#include "common.h"

bool wordBreak(char * s, char ** wordDict, int wordDictSize){
    if (wordDictSize == 0) return false;

    int  len = strlen(s);
    bool arr[len + 1];
    int  wordDictLen[wordDictSize];

    arr[0] = true;
    memset(arr + 1, 0, sizeof(bool) * len);

    for (int i = 0; i < wordDictSize; i++)
        wordDictLen[i] = strlen(wordDict[i]);

    for (int i = 0; i < len; ++i) {
        if (arr[i]) {
            for (int j = 0; j < wordDictSize; j++) {
                int p = i + wordDictLen[j];
                if (p < len + 1) {
                    char temp = s[p];

                    s[p]   = NULL;
                    arr[p] = arr[p] || (strcmp(s + i, wordDict[j]) == 0);
                    s[p]   = temp;
                }
            }
        }
    }

    return arr[len];
}