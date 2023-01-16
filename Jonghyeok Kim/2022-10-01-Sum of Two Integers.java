class Solution {
    public int getSum(int a, int b) {
        int tmp;
        while (b != 0){
            tmp = a;
            a = a ^ b;
            b = (tmp&b) << 1;
        }
        return a;
    }
}