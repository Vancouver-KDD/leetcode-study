
// input : nums = [1, 2, 3, 1] , output : true
// input: nums = [1, 2, 3, 4], output: false

//2023-01-14
//Time Complexity: O(n)
//Space Complexity: O(n)
class Solution{
    public boolean containsDuplicate(int[] nums){
        if(nums == null || nums.length == 0){
            return false;
        }

        HashSet<Integer> integerSet = new HashSet<>();

        for(int num : nums){
            if(integerSet.contains(num)){
                return true;
            }else{
                integerSet.add(num);
            }
        }

        return false;
    }
}