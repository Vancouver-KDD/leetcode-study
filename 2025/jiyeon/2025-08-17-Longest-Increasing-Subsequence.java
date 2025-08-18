import java.util.*;

class LongestIncreasingSubsequence {
    public int lengthOfLIS(int[] nums) {
        List<Integer> list = new ArrayList<>();
        for (int num : nums) {
            int idx = Collections.binarySearch(list, num);
            if (idx < 0) idx = -(idx + 1);
            if (idx == list.size()) {
                list.add(num);
            } else {
                list.set(idx, num);
            }
        }
        return list.size();
    }
}

