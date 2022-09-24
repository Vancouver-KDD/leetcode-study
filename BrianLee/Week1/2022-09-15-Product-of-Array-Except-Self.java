class Solution {
    public int[] productExceptSelf(int[] nums) {
        int allProduct = 1;
        int zeroCount = 0;
        for(int num : nums) {
            if(num == 0) zeroCount++;
            else allProduct *= num;

            if(zeroCount > 1) {
                allProduct = 0;
                break;
            }
        }

        int[] result = new int[nums.length];
        if(allProduct != 0) {
            for(int i = 0; i < nums.length; i++) {
                if(nums[i] == 0) result[i] = allProduct;
                else if(zeroCount == 1) result[i] = 0;
                else result[i] = allProduct / nums[i];
            }
        }
        return result;
    }
}