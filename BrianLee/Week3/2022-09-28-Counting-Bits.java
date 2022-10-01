class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n+1];
        for(int i = 0; i <= n; i++) {
            result[i] = getOneCount(i);
        }
        return result;
    }

    private int getOneCount(int number) {
        int count = 0;
        int one = 1;
        for(int i = 0; i < 32; i++) {
            if((number & one) == 1) {
                count++;
            }
            number >>= 1;
        }
        return count;
    }
}