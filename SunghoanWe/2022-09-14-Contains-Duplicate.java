import java.util.HashSet;

public class ContainsDuplicate {
	public static void main(String args[]) {
		//int[] nums = {1,1,1,3,3,4,3,2,4,2};
		int[] nums = {1,2,3};
		System.out.println(new ContainsDuplicate().containsDuplicate(nums));
	}
	
    public boolean containsDuplicate(int[] nums) {
        //List <Integer> temp = new ArrayList<>();
        HashSet temp = new HashSet();
        for (int i=0; i<nums.length; i++) {
        	if (temp.contains(nums[i])) {
        		return true;
        	} else {
        		temp.add(nums[i]);
        	}
        }
        return false;

    }

}
