
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
