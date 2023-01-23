import java.util.Arrays;

public class LongestConsecutiveSequence {
	  public int longestConsecutive(int[] nums) {
	        Arrays.sort(nums);
	    	int count =1;
	    	for(int i = 0 ; i < nums.length-1;i++)
	    	{
	    		if(nums[i] == nums[i+1]-1)
	    		{
	    			count++;
	    		}
	    	}
	    	return count;
	    }
}
