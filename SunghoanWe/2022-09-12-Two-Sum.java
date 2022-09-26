import java.util.HashMap;
import java.util.Map;
 
public class TwoSum {
	public static void main(String args[]) {
		int[] input= {1,3,5,6};
		int target = 4;
		
		TwoSum ts = new TwoSum();
		ts.twoSum(input, target);
	}
	
    public int[] twoSum(int[] nums, int target) {
        for (int i=0; i < nums.length; i++) {
            for (int j=0; j < nums.length; j++) {
            	if (i==j) {
            		continue;
            	} else {
            		if (nums[i]+nums[j] == target) {
                        return new int[] {i, j};
            		}
            	}
            }
        }
        return null;
    }
    
    public int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int temp = target - nums[i];
            if (map.containsKey(temp)) {
                return new int[] { map.get(temp), i };
            }
            map.put(nums[i], i);
        }
        
        return null;
    }    
	
}
