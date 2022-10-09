class Solution {
    public int maxProduct(int[] nums) {
        int min = 1;
        int max = 1;
        int result = Integer.MIN_VALUE;

        for(int num: nums) {
            int preMax = max;
            max = Math.max(num, Math.max(max * num, min * num));
            min = Math.min(num, Math.min(preMax * num, min * num));
            result = Math.max(result, max);
        }
        return result;
    }
}