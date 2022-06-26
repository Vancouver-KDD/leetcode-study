class Solution {
    public int missingNumber(int[] nums) {
        Arrays.sort(nums);
        int end = nums.length;
        int flag = 0;
        for(int i = 0; i<nums.length; i++) {
            if(nums[i] != flag) return flag;
            flag++;
        }
        return end;
    }
}