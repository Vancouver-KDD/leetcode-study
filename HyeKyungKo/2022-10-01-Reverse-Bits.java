//Important: Java does not have a datatype for unsigned integers.

//Time complexity : O(1) <-- fixed number : 32
// Space complexity: O(1) <-- only local value
public class Solution {
    // you need treat n as an unsigned value
    public int reverseBits(int n) {
        
        int reverse = 0;
        int mask = 1;
        int count = 0;
        
        while(count < 32){
            reverse = reverse << 1;
            reverse += (n & mask);
            n = n >> 1;
            count++;
        }
        return reverse;

    }
}