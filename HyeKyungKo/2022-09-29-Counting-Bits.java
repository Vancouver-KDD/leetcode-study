//2022.09.29
// limitation: n shouldn't be negative.
// Input: n = 2  -> Output: [0,1,1]
// Input: n = 5  -> Output: [0,1,1,2,1,2]

//Time complexity: O(n) , Space Complexity: O(1) <- the output array does not count
class Solution{
    public int[] countBits(int n){
        
        int[] result = new int[n+1];
        int i = 1; 
        // 0101
        // 0100

        //result[0] = 0, 
        // result[1] = result[1 & 0] + 1 = result[0] + 1 = 1
        // result[2] = result[2 & 1] + 1 = result[0] + 1 = 1   
        // result[3] = result[3 & 2] + 1 = result[2] + 1 = 2
        // result[4] = result[4 & 3] + 1 = result[0] + 1 = 1
        // result[5] = result[5 & 4] + 1 = result[4] + 1 = 2
        result[0] = 0;
        while( i <= n){
            result[i] = result[i & (i-1)] + 1;
            i++;
        }
        
        return result;
    }
}

// Time Complexity 가 이해가 잘 안되었음. 
// Time complexity: O(n⋅logn). 
// For each integer xx, in the worst case, we need to perform O(logn) operations, since the number of bits in xx equals to (log(x) + 1) and all the bits can be equal to 1. However, on average, each bit will be set n/2 times, so for each integer 'x' we will perform log(x)/2 operations, therefore, in total, it will cost O(n⋅log(n)/2) operations.
//Space Complexity: O(1)
/*
class Solution {
    public int[] countBits(int n) {
        
        if(n < 0){
            return new int[0];
        }
        
        int[] result = new int[n+1];
        int i = 0;
        while(i <= n){
            result[i] = hammingWeight(i);
            i++;
        }
        
        return result;
    }
    
    private int hammingWeight(int n){
        
        int totalBitOnes = 0;
        
        while( n != 0){
            n = n&(n-1);
            totalBitOnes++;
        }
        return totalBitOnes;
    }
}
*/