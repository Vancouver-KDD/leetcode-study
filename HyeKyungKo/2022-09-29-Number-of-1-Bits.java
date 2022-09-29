
//2022.09.29
//limitation : ???
// Input: n = 11 ( 00000000000000000000000000001011 ) -> Output: 3
// Input: n = 128  ( 00000000000000000000000010000000 ) -> Output: 1
// Time Complexity: O(1) <- 최악의 경우가 32bit 모두 1인 경우로 32번 while 문 도는 것인데. 
//                          최악의 경우가 32로 일정하니. O(1)
// Space Complexity: O(1)
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        
        int totalOneBits = 0;
        
        while(n != 0){
            n = n & (n-1);  
            totalOneBits++;
            
        }

        return totalOneBits;
    }
}