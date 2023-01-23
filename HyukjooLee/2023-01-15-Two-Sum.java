/**
 * Given an array of integers nums and an integer target, 
 * return indices of the two numbers such that they add up to target.
 */

// 1. simple solution - brute force approach
// time complexity is O(N^2) as we iterate the array twice starting with the different index
class Solution {
    public int[] twoSum(int[] nums, int target) {
        for(int i = 0; i < nums.length; i++) {
            for(int j = i + 1; j < nums.length; j++) {
                if(target == nums[i] + nums[j]) {
                    return new int[] {i,j};
                }
            }
        }
        return null;
    }
}

// 2. using HashMap
    public int[] twoSum(int[] nums, int target) {
    	Map<Integer, Integer> map = new HashMap<>();
    	for (int i = 0; i < nums.length; i++) {
    		int current = nums[i];
    		// current + x = target
    		int x = target - current;
    		if(map.containsKey(x)) {
    			return new int[] {map.get(x), i};
    		}
    		map.put(current, i);
		}
    	return null;
    }