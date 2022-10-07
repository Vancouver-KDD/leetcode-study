class Solution {
    public int lengthOfLIS(int[] nums) {
        Map<Integer,Integer> valueCount = new HashMap<>();
        int subCount = 0;
        for(int num: nums) {
            int big = 1;
            for(int value : valueCount.keySet()) {
                if(value < num) {
                    big = Math.max(big, valueCount.get(value)+1);
                }
            }
            valueCount.put(num, big);
            subCount = Math.max(big, subCount);
        }
        return subCount;
    }
}