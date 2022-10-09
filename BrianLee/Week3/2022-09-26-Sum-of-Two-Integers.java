class Solution {
    public int getSum(int a, int b) {
        for(int i = 0; i < 32; i++) {
            int tmp = (a & b) << 1;
            a = (a ^ b);
            b = tmp;
        }
        return a;
    }
}