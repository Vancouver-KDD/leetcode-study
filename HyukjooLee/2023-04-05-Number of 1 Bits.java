// Write a function that takes the binary representation of an unsigned integer 
// and returns the number of '1' bits it has (also known as the Hamming weight).

// Note:

// Note that in some languages, such as Java, there is no unsigned integer type. 
// In this case, the input will be given as a signed integer type. 
// It should not affect your implementation, 
// as the integer's internal binary representation is the same, whether it is signed or unsigned.
// In Java, the compiler represents the signed integers using 2's complement notation. 
// Therefore, in Example 3, the input represents the signed integer. -3.

// Input: n = 00000000000000000000000000001011
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.

// '1' bit 의 수를 세는 문제
// time complexity of this solution is O(logN) since we perform the bitwise & operation only on the '1' bits in n
// space complexity is O(1) because we use only variables; count, n
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int count = 0;
        while (n != 0) {
            count++;
            // n과 n - 1 사이에 비트 & 을 수행하여 n의 맨 오른쪽 '1' 비트를 0으로 설정
            // => n의 맨 오른쪽 '1' 비트를 '0'으로 뒤집고 다른 모든 비트는 변경하지 않은 상태
            n &= n - 1;
        }
        return count;
    }
}