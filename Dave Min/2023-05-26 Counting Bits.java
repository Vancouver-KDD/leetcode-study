class Solution {
    public int[] countBits(int n) {
        int result[] = new int[n+1];
        while(n!=0){
            result[n] = hamingWeight(n);
            n--;
        }
        return result;
    }
    public int hamingWeight(int n){
        int cnt=0;
        while(n!=0){
            cnt = cnt + ((n&1)==1 ? 1:0);
            n>>=1;
        }
        return cnt;
    }
}
