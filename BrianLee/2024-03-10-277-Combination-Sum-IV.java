https://leetcode.com/problems/combination-sum-iv/

class Solution {
    public int combinationSum4(int[] nums, int target) {
        return combinationSum(nums, target, new HashMap<>());
    }


    private int combinationSum(int[] nums, int left, Map<Integer, Integer> mem) {
        if(left == 0) return 1;
        else if(left < 0) return 0;
        if(mem.containsKey(left)) return mem.get(left);

        int sub = 0;
        for(int num: nums) {
            sub += combinationSum(nums, left-num, mem);
        }
        mem.put(left, mem.getOrDefault(left, 0)+sub);
        return mem.get(left);
    }
}
