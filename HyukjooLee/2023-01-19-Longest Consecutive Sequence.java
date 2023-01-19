/**
 * Given an unsorted array of integers nums, 
 * return the length of the longest consecutive elements sequence.
 * You must write an algorithm that runs in O(n) time.
 */

// 1. sorting array and check if the current element is consecutive to the previous one
// if it is, increment the current sequence count by 1
// if it isnt, reset the current sequence after updating the longestCount
// time complexity is O(N * logN) as we traverse the nums array(N) after sorting(logN) of the array
class Solution {
    public int longestConsecutive(int[] nums) {
        // sort the array
        Arrays.sort(nums);
        int longestCount = 1;
        int currentCount = 1;
        // iterate over the array, checking if the current element is consecutive
        for(int i = 1; i < nums.length; i++) {
            if (nums[i] == nums[i-1] + 1) {
                currentCount++;
            } else {
                // 
                longestCount = Math.max(longestCount, currentCount);
                currentCount = 1;
            }
        }
        return Math.max(longestCount, currentCount);
    }
}

// 2. using HashSet to store elements of input array; 중복값 x, contains method
// check it is the first element in sequence
// if it is, start counting consecutive elements keeping track of the longest sequence
// time complexity is O(N) as we convert the input array to a HashSet in O(N) time
// and iterate over the hashset 
class Solution {
    public static int longestConsecutive(int[] nums) {
		Set<Integer> set = new HashSet<>();
        // add elements to hashset
		for (int num : nums) {
			set.add(num);
		}
		int longestCount = 0;
		// iterate the set
		for (int num : set) {
			// consecutive elements 시작점인지 check
			if (!set.contains(num - 1)) {
				int beginNum = num;
				int currentCount = 1;
				// keep counting consecutive elements
				while (set.contains(beginNum + 1)) {
					beginNum++;
					currentCount++;
				}
				longestCount = Math.max(longestCount, currentCount);
			}
		}
		return longestCount;
	}

