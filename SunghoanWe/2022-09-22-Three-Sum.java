import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class ThreeSum {
 
	public static void main(String[] args) {
		// TODO Auto-generated method stub

	}

    public List<List<Integer>> threeSum(int[] nums) {
    	List<List<Integer>> result = new ArrayList<>();
    	Arrays.sort(nums);
    	
        for (int i = 0; i < nums.length; i++) {
            int sum = -nums[i];
            int front = i + 1;
            int back = nums.length - 1;
            while (front < back) {
                if (sum > nums[front] + nums[back]) {
                    front++;
                }
                else if (sum < nums[front] + nums[back]) {
                    back--;
                }
                else {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[front]);
                    triplet.add(nums[back]);
                    result.add(triplet);

                    while (front < back && nums[front] == triplet.get(1)) {
                        front++;
                    }
                    while (front < back && nums[back] == triplet.get(2)) {
                        back--;
                    }
                }
            }
            while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
                i++;
            }
        }
        return result;
     }
    
    
    public List<List<Integer>> threeSum2(int[] nums) {
    	List<List<Integer>> result = new ArrayList<>();
    	Arrays.sort(nums);
    	
        for (int i = 0; i < nums.length; i++) {
            int sum = nums[i];
            int front = i + 1;
            int back = nums.length - 1;
            while (front < back) {
                if (sum > nums[front] + nums[back]) {
                    front++;
                }
                else if (sum < nums[front] + nums[back]) {
                    back--;
                }
                else {
                    List<Integer> triplet = new ArrayList<>();
                    triplet.add(nums[i]);
                    triplet.add(nums[front]);
                    triplet.add(nums[back]);
                    result.add(triplet);

                    while (front < back && nums[front] == triplet.get(1)) {
                        front++;
                    }
                    while (front < back && nums[back] == triplet.get(2)) {
                        back--;
                    }
                }
            }
            while (i + 1 < nums.length && nums[i + 1] == nums[i]) {
                i++;
            }
        }
        return result;
     }    
}
