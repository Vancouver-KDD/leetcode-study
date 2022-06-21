public class Solution {
    public int HammingWeight(uint n) {
        int numOnes=0;
        uint currDigit;
        while(n != 0){
            currDigit = n & 1;
            if(currDigit==1){
                numOnes++;
            }
            n = n >> 1;
        }
        return numOnes;
    }
}