class Solution {
public:
    int getSum(int a, int b) {

        // Half Adder
        // Carry = A AND B
        // Sum = A XOR B
        
        while(b!=0){
            unsigned c = a & b;     // carry
            a = a ^ b;              // HA sum = a xor b
            b = c << 1;             // bit shift for carry
        }
        return a;
    }
};