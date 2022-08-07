#include "common.h"

int characterReplacement(char * s, int k) {
    int arr[26] = {0};
    int start = 0, end = 0;

    int replacement = 0;
    int max_len = 0;
    int count = 0;
    bool slide_end = true;

    while(s[end] != '\0') {
        if (slide_end) arr[s[end] - 'A'] += 1;

        int frequent = 0;
        for(int i = 0; i < 26; i++) {
            if(arr[i] >= frequent) frequent = arr[i];
        }

        replacement = (end - start + 1) - frequent;

        if(replacement <= k) {
            slide_end = true;
            count++;
            end++;
        }
        else {
            slide_end = false;
            arr[s[start] - 'A'] -= 1;
            count--;
            start++;
        }

        if(count >= max_len) max_len = count;
    }


    return max_len;
}
