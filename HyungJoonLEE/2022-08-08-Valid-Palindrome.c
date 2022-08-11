#include "common.h"

bool isPalindrome(char * s){
    int len = strlen(s);
    if(!len) return true;
    char *p1 = s, *p2 = s + len - 1;
    while(p1 < p2){
        if(!isalnum(*p1)) {
            p1++;
            continue;
        }
        if(!isalnum(*p2)) {
            p2--;
            continue;
        }
        if(tolower(*p1++) != tolower(*p2--)) return false;
    }
    return true;
}
