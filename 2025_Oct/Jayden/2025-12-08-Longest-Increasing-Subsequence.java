class Solution {
    /**
        Time Complexity: O(n^2)
        Space Complexity: O(n)
     */
    public int lengthOfLIS(int[] nums) {
        int[] dp = new int[nums.length];
        Arrays.fill(dp, 1);

        for (int i = 0; i < nums.length; i++) {
            // finding the max LIS
            for (int j = 0; j < i; j++) {

                // if nums[j] < nums[i], we can extend the LIS
                if (nums[j] < nums[i]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
            }
        }

        int maxLength = 1;
        for (int length : dp) {
            maxLength = Math.max(maxLength, length);
        }

        return maxLength;
    }
}


class Solution {
    /**
        Time Complexity: O(nlogn)
        Space Complexity: O(n)
     */
    public int lengthOfLIS(int[] nums) {
        List<Integer> result = new ArrayList<>();

        for (int num : nums) {
            int left = 0;
            int right = result.size();

            while (left < right) {
                int mid = (left + right) / 2;
                if (num <= result.get(mid)) {
                    right = mid;
                } else {
                    left = mid + 1;
                }
            }

            // extend the sequence if num is larger than all elements
            if (left == result.size()) {
                result.add(num);
            } else {
                // replace the element at left index to make the tail smaller
                result.set(left, num);
            }
        }

        return result.size();
    }

}