class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        
        uint32_t res = 0;
        
        // iterate over each bit
        for(int i=0; i<32; i++){
            
            // i-th bit from LSB
            uint32_t bit_curr = (n>>i) & 1;
            
            // left shit and add to LSB
            res = (res<<1) + bit_curr;
        }
        return res;
    }
};