// Given an integer n, return an array ans of length n + 1 
// such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

// Input: n = 2
// Output: [0,1,1]
// Explanation:
// 0 --> 0
// 1 --> 1
// 2 --> 10

// 0에서 n 까지의 각 정수의 이진 표현에서 1 비트 수를 계산하고 그 결과를 배열에 저장하고 리턴
// => 0에서 n 까지 반복하면서 각 index 에 대한 이진 표현에서 1 비트 수를 계산
// time complexity is O(N logN), iterate through its bits in its binary representation
// space complexity is O(N); result array of size n + 1
public class Solution {
    public int[] countBits(int n) {
        int[] result = new int[n + 1];
        
        for (int i = 0; i <= n; i++) {
            int current = i;
            int count = 0;
            
            while (current != 0) {
                if ((current & 1) == 1) {
                    count++;
                }
                current = current >> 1;
            }
            
            result[i] = count;
        }
        
        return result;
    }
}
