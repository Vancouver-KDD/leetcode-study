class Solution {
    public int rob(int[] nums) {
        if(nums == null || nums.length == 0) return 0;
        if(nums.length == 1) return nums[0];
        if(nums.length == 2) return Math.max(nums[0], nums[1]);


        int[] mem = new int[nums.length];
        for(int i = 0; i < nums.length; i++) mem[i] = -1;

        int result1 = fun(nums.length-1, nums, mem);
        if(mem[nums.length-1] == mem[nums.length-2]) return result1;

        result1 = Math.max(mem[nums.length-1]-nums[nums.length-1], mem[mem.length-2]);
        for(int i = 0; i < nums.length; i++) mem[i] = -1;
        nums[0] = 0;
        int result2 = fun(nums.length-1, nums, mem);
        return Math.max(result1, result2);
    }

    private int fun(int n, int[] nums, int[] mem) {
        if(n == 0) return nums[0];
        if(n == 1) return Math.max(nums[0], nums[1]);

        if(mem[n] != -1) return mem[n];
        return mem[n] = Math.max(fun(n-2, nums, mem) + nums[n], fun(n-1, nums, mem));
    }
}