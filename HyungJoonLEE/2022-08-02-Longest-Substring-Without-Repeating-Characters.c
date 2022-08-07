#include "common.h"


int lengthOfLongestSubstring(char * s){
    int arr[128], index = 128;
    while (index--) arr[index] = -1;

    int start = -1, length = 0, localLength;
    size_t c;

    while (s[++index] != NULL) {
        c = (size_t) s[index];
        if (arr[c] > start) start = arr[c];

        localLength = index - start;
        if (length < localLength) length = localLength;
        arr[c] = index;
    }
    return (start > -1 ? length : index);
}