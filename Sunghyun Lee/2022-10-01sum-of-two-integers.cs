public class Solution {
    public int GetSum(int a, int b) {
        int bitwiseAnd = b;
        int result = a;
        while(bitwiseAnd != 0)
        {
            int temp = result ^ bitwiseAnd ;
            bitwiseAnd = (result & bitwiseAnd) << 1;
            result = temp;
        }
            
        return result;
    }
}
