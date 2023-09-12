//limitation: the array is sorted??? no ??? is it Ok if I sort the array?
//idea: 
// 먼저 입력 배열을 sorting 한뒤, 
// twoSum 방식을 이용해서 풀거나, 또는 twoSumII 방식을 이용해서 풀 수 있다. 둘다 가능. 
//  3sum solution : first, make sorted array. Next, using 2 pointers solution 
//  2 pointer solution : array should be sorted. 
//                       start position is '0 ', end position is 'length -1'
//                       if(nums[start] + nums[end] <= target){ 
//							if(nums[start] + nums[end] == target){
//								//add 3 numbers to the result list
//							}
//							start++ ...
//						 } 
//						 else {end-- ...}
//  important: check the repeated number and need to skip them. 

//Time Complexity: O(N^2) : for (while)
//Space Complexity: from O(log⁡n) to O(n) <-- Space used for sorting 

 class Solution{

    public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> result = new ArrayList<>();
        if(nums == null || nums.length < 3 ){
            return result; //empty list
        }

        Arrays.sort(nums); 

        for(int i = 0; i < nums.length -2; i++ ){
            //skip same number
            if(i > 0 && nums[i] == nums[i-1]){
                continue;
            }
            twoSumII(nums, i, result);
        }

        return result;
    }

    void twoSumII(int[] nums, int index, List<List<Integer>> result){

        int start = index+1;
        int end = nums.length -1;
        while(start < end){
            int sum = nums[index] + nums[start] + nums[end];
            if(sum > 0){
                end--;
            }else if(sum < 0){
                start++;
            }else{ // sum == 0
                result.add(Arrays.asList(nums[index], nums[start], nums[end]));
                start++;
                end--;
                //skip same number
                while(start < end && nums[start] == nums[start -1]){
                    start++;
                }
            }
        }
    }
}