// Given two integers a and b, return the sum of the two integers without using the operators + and -.

// Example 1:
// Input: a = 1, b = 2
// Output: 3

// Constraints:

// -1000 <= a, b <= 1000

// without + , - operators?
// using bitwise operation?

// 음...
// 두 정수의 합을 구하는데 +, - 를 사용하지마라
// 0000 0101 (5)
// 0000 0011 (3)
// =>
// 0000 1000 (8)

// 5 a
// 3 b

// 0101 a
// 0011 b

// After XOR operation (*Step 1)

// 0110 a ^ b - XOR result

// After AND operation and left shift the result by 1 (*Step 2)

// (a & b) << 1;

// 0101 a
// 0011 b

// (a & b)
// 0001
// << 1
// 0010 - left shift the result

// repeat Step 1 and 2 using the XOR result (0110) and the left-shifted carry result (0010).

// ...

// 1000 - at this point, we have no carry bits left (the XOR result is 0000), so the loop stop

// time complexity is O(log(max(a, b)))
// space complexity is O(1) as we are using a constant amount
public class Solution {
    public int getSum(int a, int b) {
        while (b != 0) {
            int sumWithoutCarry = a ^ b;
            int carry = (a & b) << 1;
            a = sumWithoutCarry;
            b = carry;
        }
        return a;
    }
}