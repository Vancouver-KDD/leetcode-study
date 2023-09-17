import java.util.Arrays;

class Solution {
    public int threeSumClosest(int[] nums, int target) {

        Arrays.sort(nums);
        int closest = nums[0]+nums[1]+nums[2];

        for(int i = 0; i < nums.length-2; i++) {
            int j = i + 1;
            int k = nums.length-1;

            while(j < k) {
                int val = nums[i] + nums[j] + nums[k];

                if(val == target) {
                    return val;
                }
                closest = Math.abs(target-val) < Math.abs(target-closest) ? val : closest;
                
                if(target - val < 0) {
                    k--;
                }
                else {
                    j++;
                }
            }
        }
    
        return closest;
    }
}