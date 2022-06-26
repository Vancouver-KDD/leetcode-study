public class Solution {
    public int[] CountBits(int n) {
        
        int[] bitsList = new int[n+1];
        
        bitsList[0] = 0;
        
        for(int i=1; i<=n; i++){
        
            if((i%2) == 1){
                bitsList[i] = bitsList[i/2]+1;
            } else {
                bitsList[i] = bitsList[i/2];
            }
        }
        
        return bitsList;
        
    
        
    }
}