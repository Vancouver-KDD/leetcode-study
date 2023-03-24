class Solution {
    public int rob(int[] nums) {
        //if (nums == null || nums.length == 0) return 0;
        if (nums.length == 1) return nums[0];
    
        // base cases: handle first two houses manually
        int with = nums[1];                           // max val for houses [0, i] with robbing house i
        int without = nums[0];                        // max val for houses [0, i] without robbing house i
        int withNoFirst = nums[1];                    // max val for houses [1, i] with robbing house i
        int withoutNoFirst = 0;                       // max val for houses [1, i] without robbing house i 
        
        for (int i = 2; i < nums.length - 1; ++i) {
            int oldWith = with;
            with = without + nums[i];
            without = Math.max(oldWith, without);
            
            int oldWithNoFirst = withNoFirst;
            withNoFirst = withoutNoFirst + nums[i];
            withoutNoFirst = Math.max(oldWithNoFirst, withoutNoFirst);
            
        }
        
        // handle last house nums[nums.length - 1] manually
        return Math.max(Math.max(with, without), withoutNoFirst + nums[nums.length - 1]);
    }
}