class Solution {
    public boolean canJump(int[] nums) {
        return fun(nums, 0, new Boolean[nums.length]);
    }

    private boolean fun(int[] nums, int cur, Boolean[] mem) {
        if(mem[cur] != null) return mem[cur];
        if(cur >= nums.length-1) return true;

        for(int i = cur+1; i <= cur+nums[cur]; i++) {
            if(fun(nums, i, mem)) return mem[cur] = true;
        }
        return mem[cur] = false;
    }
}