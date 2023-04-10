
class Solution {
    public boolean canJump(int[] nums) {
        //at the end of the day, max has to be bigger than index
        int max = 0;
        for(int i = 0; i<nums.length;i++) {
            if(i>max) return false; //max can't reach to the index 
            max = Math.max(nums[i] + i, max);
        }
        return true;
    }
}

//TC  : O(N)