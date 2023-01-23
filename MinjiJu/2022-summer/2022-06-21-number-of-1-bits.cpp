class Solution {
public:
    int hammingWeight(uint32_t n) {
        
        int count = 0;
        
        while(n>0){
            count += n & 1; // increment counter if 1 found
            n >>= 1;        // bitshift n
        }
        
        return count;
    }
};