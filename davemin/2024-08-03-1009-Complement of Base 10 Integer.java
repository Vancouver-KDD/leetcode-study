class Solution {
    public int bitwiseComplement(int n) {
        if(n==0)return 1;
        int num=0;
        while(num<n){
            num=(num<<1)|1;

        }
      return ~n&num;
    }
}
