//Using for-loop
public class TwoSum {

	class Solution {
	    public int[] twoSum(int[] nums, int target) {
	        int[] output = new int[2];
	        for (int i=0; i<nums.length-1; i++){
	            for (int j=1+i; j<nums.length; j++){
	                if ((nums[i]+nums[j]) == target){
	                    output[0]=i;
	                    output[1]=j;
	                    break;
	                }
	            }
	        }
	        
	        return output;
	    }
	}
}

//Using HashMap
class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer, Integer> HM = new HashMap<>();
        for (int i=0; i<nums.length; i++){
            int com = target - nums[i];
            
            if (HM.containsKey(com)){
                return new int[]{i, HM.get(com)};
            } else{
                HM.put(nums[i], i);
            }
        }
        return null;
    }
}
