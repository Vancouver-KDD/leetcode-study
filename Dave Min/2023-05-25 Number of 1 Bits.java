public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        //solution 1
        //integer is 4 byte -> 32 bit
        int cnt=0;
        int comparer =1;
        for(int i=0;i<32;i++){
            System.out.println(n & comparer);
            if((n & comparer) != 0) cnt++;
            comparer <<= 1;
        }
        return cnt;
        //TC O(1);
        //SC O(1);

        //solution2
        //..1110100 -> n
        //..1110011 -> n-1
        //so when n & n-1 the least significant bit 1 can be removed.
        //..1110000
        //..1101111
        // until n ==0

        // int cnt = 0;
        // while(n!=0){
        //     cnt++;
        //     n = n & (n-1);
        // }

        // return cnt;
        //TC O(1);
        //SC O(1);
    }
}

