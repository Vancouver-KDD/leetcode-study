#include "common.h"


int combination (int num1, int num2) {
    num2 = num1 - num2 < num2 ? num1-num2 : num2;
    long ans = 1;
    for(int i = 0; i < num2; i++) {
        ans *= num1 - i;
        ans /= i + 1;
    }
    return (int) ans;
}

int climbStairs(int n) {
    int two = 0, total = 0, step = 0;
    for (two = 0; two * 2 <= n; two++) {
        step = n - two;
        total += combination(step, two);
    }
    return total;
}
