#include "common.h"


int hammingWeight(uint32_t n) {
    int count = 0;
    while (n != 0) {
        if (n - ((n >> 1) << 1) == 1) count++;
        n = n >> 1;
    }
    return count;
}


int hammingWeight2(uint32_t n) {
    int count = 0;
    while (n != 0) {
        if ((n & 1) == 1) count++;
        n = n >> 1;
    }
    return count;
}


int hammingWeight3(uint32_t n) {
    int count = 0;
    for (int i = 0; i < 32; i++) {
        if ((n & 1) == 1) count++;
        n = n >> 1;
    }
    return count;
}