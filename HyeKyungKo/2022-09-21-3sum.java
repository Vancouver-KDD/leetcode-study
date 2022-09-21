// limitation: if nums is null or size is 0, return null
// Input: nums = [-1,0,1,2,-1,-4] , Output: [[-1,-1,2],[-1,0,1]]
// Input: nums = [0,1,1] , Output: []

//Time Complexity: O(n^2)    
// Space Complexity: O(n) <---  Sorting 하는데 든 메모리라고 하네  (java 는 array sort 를 위해 quicksort 를 쓰는데 time complexity: O(nlogn) , space complexity: O(n) , 사실 time complexity 도 quick sort 의 worst case 는 O(n^2) 인데 java 에서는 개선된 것을 써서 n^2 가 발생하지 않고 worst case 가 nlogn 되게 해준다고 함. )
//2022.09.21
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        if(nums == null || nums.length < 3){
            return null;
        }
        
        List<List<Integer>> threeSumList = new ArrayList<List<Integer>>();
        
        Arrays.sort(nums); //To remove duplicated cases
        
        for(int i = 0; i < nums.length; i++){
            if( (i > 0) && (nums[i] == nums[i-1])){
                //skip the duplicated case
                continue;
            }
            
            int target = nums[i] * -1;  // target is the number to make sum as zero
            int start = i +1;
            int end = nums.length -1;
            
            while(start < end){
                int sum = nums[start] + nums[end];
                if(sum == target){ // find 3sum
                    List<Integer> eachList = Arrays.asList(nums[i], nums[start], nums[end]);
                    threeSumList.add(eachList);
                    
                    start++;
                    end--;
                    //To avoid duplication                
                    while((start < nums.length-1) && nums[start-1] == nums[start]){
                        start++;
                    }  
                    while((end > start) && nums[end] == nums[end+1]){
                        end--;
                    }
                    
                }else if(sum > target){
                    end--;
                }else{//sum < target
                    start++;
                }
             
            }
            
        }
        
        return threeSumList;
    }
}