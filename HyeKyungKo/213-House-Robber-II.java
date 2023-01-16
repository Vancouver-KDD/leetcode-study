//2022-12-04
//Time Complexity :O(N)
//Space Complexity: O(1)
class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0){
            return 0;
        }

        if(nums.length == 1){
            return nums[0];
        }else if(nums.length == 2){
            return Math.max(nums[0], nums[1]);
        }
        
        int max1 = rob(nums, 0, nums.length-2);
        int max2 = rob(nums, 1, nums.length-1);
        return Math.max(max1, max2);
    }

    private int rob(int[] nums, int start, int end){
        int prevPrev = 0;
        int prev = 0;
        int max = 0;
        for(int i = start; i <= end; i++){
            max = Math.max(prev, prevPrev+nums[i] ); // i번째 집을 rob 안할경우와, 할 경우에서 최대값 선택
            prevPrev = prev;
            prev = max;
        }

        return max;
    }
}