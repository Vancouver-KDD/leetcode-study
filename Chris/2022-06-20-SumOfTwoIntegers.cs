public class Solution {
    public int GetSum(int a, int b) {
        int tmpA;
        while(b != 0){
            tmpA = a;
            a = tmpA ^ b;
            b = (tmpA & b) << 1;
        }
        
        return a;
        
        
    }
}