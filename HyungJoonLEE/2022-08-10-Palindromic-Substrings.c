#include "common.h"

int countSubstrings(char *s) {
    int result = 0;
    int length = strlen(s);

    for(int i = 0; i < length; i++) {
        int i_left = i;
        int i_right = i;

        // Odd length
        while(i_left >= 0 && i_right < length && s[i_left] == s[i_right]) {
            i_left--;
            i_right++;
            result++;
        }

        // Even length
        i_left = i;
        i_right = i+1;
        while(i_left >= 0 && i_right < length && s[i_left] == s[i_right]) {
            i_left--;
            i_right++;
            result++;
        }
    }

    return result;
}
