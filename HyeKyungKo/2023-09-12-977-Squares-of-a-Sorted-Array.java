//2023-09-12
//limitation : the array has distinct numbers? --> maybe not 
// 작업을 2번 하면 되지 않을까?  첫번째, square 를 만든다(absolute value 가 됨). 두번째, 2 point 방식으로 sorting 을 한다. 
// example: 
// Input: nums = [-4,-1,0,3,10]  -> 16, 1, 0, 9, 100
//      => 2-point방식 :  first number is start, last number is end.  

//Time Complexity: O(N) 
//Space Complexity: O(N) <-- it is only for return array
class Solution {
    public int[] sortedSquares(int[] nums) {
        if(nums == null || nums.length <= 0){
            return null;
        }

        int[] sortedSquares = new int[nums.length];

        for(int i = 0; i < nums.length; i++){
            nums[i] *= nums[i];
        }

        //Input: nums = [-7,-3,2,3,11] -> [49, 9, 4, 9, 121]
        //(49 < 121) -> (49 > 9) -> (9 > 9) -> (9 > 4) <- (4 == 4)
        // 121 <- 49 <- 9 <- 9 <- 4
        int start = 0;
        int end = nums.length -1;
        int count = nums.length -1;
        while(start <= end){
            if(nums[start] > nums[end]){
                sortedSquares[count] = nums[start];
                start++;
            }else{
                sortedSquares[count] = nums[end];
                end--;
            }
            count--;
        }

        return sortedSquares;        
    }
}
