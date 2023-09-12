//2023-09-12
//limitation: Is the nums array sorted? -> no 
//brute force : for loop 3번, 
//  -> 속도 줄이기 위해 2 point 방식 이용 (array sort 필요) -> n^2 가능 

// example : Input: nums = [-1,2,1,-4], target = 1
// -4, -1, 1, 2 => -4 with (-1, 1, 2), 
//       start: -1, end:2  (-1, 2): 1 -> (1,2) : 3 
//     -1, 1, 2 => -1 with (1,2) => 2    ===> answer : 2

//Time Complexity: O(N^2)
//Space Complexity: from O(logN) to O(N) <-- by Sorting algorithm

class Solution{
    public int threeSumClosest(int[] nums, int target){
        if(nums == null || nums.length < 3){
            return 1001;  // ???
        }

        Arrays.sort(nums); //ascending order 

        //int closest = 1001; //이렇게 하면, target 이 1000 인 경우 closest 가 1001 로 리턴될수 있음. 
        int closest = Integer.MAX_VALUE;

        //nums = [-4, -1, 1, 2] , target = 1
        //i: -4 (-4, -1, 2):-3 -> (-4, 1, 2):-1 
        //i: -1 (-1, 1, 2): 2 
        //closest : -1 -> 2
        for(int i = 0; i < nums.length -2; i++){
            int start = i + 1;
            int end = nums.length -1;
            while(start < end){
                int sum = nums[i] + nums[start] + nums[end];
                if((target - sum) > 0){
                    start++;
                }else{
                    end--;
                }
                if(Math.abs(target - sum) < Math.abs(target - closest)){
                    closest = sum;
                }
            }
        }

        return closest;
    }
}