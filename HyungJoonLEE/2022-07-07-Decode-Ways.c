#include "common.h"


int numDecodings(char* s) {
    if (!s || s[0] == '0') return 0; // leading zero is not illegal

    int n = strlen(s);

    // r1:i+1, r2:i+2
    int current = 0;
    int r2 = 1;
    int r1 = s[n - 1] != '0' ? 1 : 0; // if the number is not 0, the combination is 1
    // loop from end to start to avoid
    for (int i = n - 2; i >= 0; i--) {
        if (s[i] == '0') current = 0;
        else if ((s[i] == '1') ||(s[i] == '2' && s[i + 1] <= '6')) // if s[i]s[i+1] <= 26, current is the sum of r1 and r2
            current = r1 + r2;
        else
            current = r1; // update the info before shifting to left
        r2 = r1;
        r1 = current;
    }
    return r1;
}