class Solution {
    public int rob(int[] nums) {
        int[] mem = new int[nums.length];
        for(int i = 0; i < nums.length; i++)
            mem[i] = -1;

        return fun(nums.length-1, nums, mem);
    }

    private int fun(int n, int[] nums, int[] mem) {
        if(n < 0) return 0;
        if(n == 0) return nums[0];
        if(n == 1) return Math.max(nums[0], nums[1]);

        if(mem[n] != -1) return mem[n];
        mem[n-2] = fun(n-2, nums, mem);
        mem[n-1] = fun(n-1, nums, mem);

        return Math.max(mem[n-2] + nums[n], mem[n-1]);
    }
}