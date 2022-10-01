//2022.09.29

//limitation : ????
// Input: a = 1, b = 2  -> Output: 3 
// Input: a = 2, b = 3  -> Output: 5

//Java integer is a number of 32 bits. 31 bits are used for the value. The first bit is used for the sign: if it's equal to 1, the number is negative, if it's equal to 0, the number is positive.
//For the representation of a negative number Java uses the so-called "two's complement":

//Time Complexity : O(1) <-- 최악의경우 32번 /32는 고정값., Space Complexity : O(1)
class Solution {
    public int getSum(int a, int b) {
        
        while( b != 0){
            int addWoCarry = a ^ b; // add without carry
            int carry = (a & b) << 1; // carry 
            a = addWoCarry;
            b = carry;           
        }

        return a;
    }
}