import java.util.*;

public class ContainsDuplicates {


	// 1. Method  -  Using Arrays.sort
   public static boolean containsDuplicate1(int[] nums) {
    	
    	Arrays.sort(nums);
    	for(int i = 0 ; i < nums.length-1;i++) {
    		if(nums[i] == nums[i+1])
    			return true;
    		
    	}
    	return false;
    }
   
   
   
   // 2. Method  -  Using two for loops
   public static boolean containsDuplicate2(int[] nums) {
   	
	   for(int i = 0 ;i < nums.length; i++)
	     {
          for(int j = i+1; j < nums.length; j++)
          {
        	  if(nums[i] == nums[j])
        	  {
        		  return true;	
        	  }
          }
        }
		        
        return false;
    }


}
