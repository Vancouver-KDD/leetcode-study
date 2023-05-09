class Solution {
    public boolean containsDuplicate(int[] nums) {
        Set<Integer> distinct = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            if(distinct.contains(nums[i])) {
                return true;
            }
            distinct.add(nums[i]);
        }
        return false;
    }
}