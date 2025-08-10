class HouseRobber {
    public int rob(int[] nums) {
        int prevRob = 0;
        int maxRob = 0;
        for (int num : nums) {
            int temp = Math.max(maxRob, num + prevRob);
            prevRob = maxRob;
            maxRob = temp;
        }
        return maxRob;
    }
}