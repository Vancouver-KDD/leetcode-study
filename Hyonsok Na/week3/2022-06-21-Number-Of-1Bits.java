public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        //The java.lang.Integer.toBinaryString() method returns a string representation of the integer argument as an unsigned integer in base 2. 
        //It accepts an argument in Int data-type and returns the corresponding binary string.
        String str = Integer.toBinaryString(n);
        int count = 0;
        for (int i = 0; i<str.length(); i++) {
            if (str.charAt(i) == '1')
                count++;
        }
        return count;
    }
}