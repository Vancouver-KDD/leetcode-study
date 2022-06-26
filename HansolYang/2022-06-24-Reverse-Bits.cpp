class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        int sqridx = 31;
        uint32_t res = 0;
        while (sqridx >= 0) {
            if (pow(2, sqridx) <= n) {
                n = n - pow(2, sqridx);
                res += pow(2, (31 - sqridx));
            }
            sqridx--;
        }
        return res;
    }
};