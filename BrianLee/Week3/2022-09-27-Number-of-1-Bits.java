public class Solution {
    public int hammingWeight(int n) {
        int count = 0;
        int one = 1;
        for(int i = 0; i < 32; i++) {
            if((n & one) == 1) {
                count++;
            }
            n >>= 1;
        }
        return count;
    }
}