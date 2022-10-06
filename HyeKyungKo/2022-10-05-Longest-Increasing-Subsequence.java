//limitation : if nums is null and size is zero, return 0 ??
//Input: nums = [10,9,2,5,3,7,101,18] ->  Output: 4

//Time Complexity: O(n^2), Space Complexity: O(n)
class Solution {
    public int lengthOfLIS(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        int[] numOfSubseq = new int[nums.length];
        int maxNum = 1; //max size of subsenquence 
        numOfSubseq[0] = 1;
        
        //i:    0  1  2  3   4   5     6   7 
        //in :  10 9  2  5   3   7    101  18
        //max:   1 1  1  2   2   3     4    4
        for(int i = 1; i < nums.length; i++){
            numOfSubseq[i] = 1;
            for(int j = 0; j < i; j++){
                if(nums[j] < nums[i]){
                    //update the max Size of subsequence until nums[i]
                    numOfSubseq[i] = Math.max(numOfSubseq[i], numOfSubseq[j] + 1);
                }
            }
            maxNum = Math.max(maxNum, numOfSubseq[i]);
        }
        
        return maxNum;
    }
}