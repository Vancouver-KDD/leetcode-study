#include "common.h"

int getSum(int a, int b){

    while (b) {
        unsigned temp = (unsigned)(a & b) << 1;
        a = a ^ b;
        b = (int)temp;
    }
    return a;
}
