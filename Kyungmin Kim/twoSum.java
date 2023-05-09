class Solution {
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> preMap = new HashMap<>();

        for(int i = 0; i < nums.length; i++){
            int num = nums[i];
            int diff = target - num;

            if(preMap.containsKey(diff)){
                return new int[] {preMap.get(diff),i};
            }
            preMap.put (num, i);
        }
        return new int[] {};
    }
}