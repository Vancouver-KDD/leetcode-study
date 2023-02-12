import java.util.*;

public class ThreeSum {
	  public List<List<Integer>> threeSum(int[] nums) {
	        HashSet<List<Integer>> set = new HashSet<>();
	        Arrays.sort(nums);

	        for(int i = 0 ; i < nums.length-1;i++)
	        {
	            int j = i+1;
	            int k = nums.length-1;
	            int sum = nums[i]+nums[j]+nums[k];
	            while(j<k)
	            {
	                if(sum ==0)
	                {
	                  	set.add(Arrays.asList(nums[i],nums[j],nums[k]));  
	                    j++;
	                    k--;
	                }else{
	                    j++;
	                    k--;
	                }
	            }

	        }
	        return new ArrayList(set);
	    }
}
