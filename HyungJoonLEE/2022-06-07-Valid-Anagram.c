#include "common.h"

#define ALPHABET 26

bool isAnagram(char * s, char * t);

int main() {
    char* s = "aacc";
    char* t = "aabb";
    isAnagram(s, t);
}


bool isAnagram(char * s, char * t) {
    int arr[ALPHABET] = {0};
    if(strlen(s) != strlen(t)) return false;
    for (int i = 0; i < strlen(s); i++) {
        arr[s[i] - 97] += 1;
        arr[t[i] - 97] -= 1;
    }
    for(int i = 0; i < ALPHABET; i++) {
        if (arr[i] != 0) return false;
    }
    return true;
}


