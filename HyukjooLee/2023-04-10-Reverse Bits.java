// Reverse bits of a given 32 bits unsigned integer.

// Note:

// Note that in some languages, such as Java, there is no unsigned integer type. 
// In this case, both input and output will be given as a signed integer type. 
// They should not affect your implementation, as the integer's internal binary representation is the same, whether it is signed or unsigned.
// In Java, the compiler represents the signed integers using 2's complement notation. 
// Therefore, in Example 2 above, the input represents the signed integer -3 and the output represents the signed integer -1073741825.


// Example 1:

// Input: n = 00000010100101000001111010011100
// Output:    964176192 (00111001011110000010100101000000)
// Explanation: The input binary string 00000010100101000001111010011100 represents 
// the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.


// Constraints:

// The input must be a binary string of length 32
 

// Follow up: If this function is called many times, how would you optimize it?
// => we can use memoization

// Given a 32-bit unsigned integer, the task is to reverse its bits. 
// 32-비트의 부호 없는 정수 뒤집는 문제
// 자바에서는 unsigned integer type 이 없으므로, input 과 output 이 signed integer types
// 으로 주어지고, 똑같이 취급해야 함
// 주어진 n bits 를 순회하면서 역순으로 배치하고 리턴

// 새로운 result integer 를 initialize 하고 
// 32 비트를 모두 순회 하면서 current i 비트를 역순으로 이동시킴

// initialize an integer 'result' to store the reversed bits
// iterate through all 32 bits of the input integer 'n'
// shift the 'result' left by 1 bit to make space for the current bit
// use bitwise AND operation with 'n' and 1 to extract the current bit
// use bitwise OR operation to combine the current bit with the 'result'
// shift the input integer 'n' right by 1 bit to process the next bit
// after the loop, return the 'result' as the reversed integer 

// the time complexity is O(1) as we are iterating through a fixed number (32) of bits 
// the space complexity is O(1); a constant amount of additional space
public class Solution {
    public int reverseBits(int n) {
        int result = 0;
        
        for (int i = 0; i < 32; i++) {
            result <<= 1;
            result |= (n & 1);
            n >>= 1;
        }
        
        return result;
    }
}
