//2023-01-18
//input: [100, 4, 200, 1, 3, 2] -> output: 4
//input: [0, 3, 7, 2, 5, 8, 4, 6, 0, 1] -> output: 9
//[idea] -> Add all nums to HashSet , then check one by one element in nums[i]
// if there is (nums[i]-1) number, skip. if not, check whether there is consecutive 
// increasing number and save the count
//Time Complexity: O(N)
//Space Complexity: O(N)
class Solution{
    public int longestConsecutive(int[] nums){
        if(nums == null || nums.length == 0){
            return 0;
        }

        HashSet<Integer> set = new HashSet<>();
        for(int num: nums){
            set.add(num);
        }

        int longestSize = 0; 
        List<Integer> result = new ArrayList<>(); // longest 배열을 저장해야 하는 경우 
        int startElement = 0; // 제일긴 배열을 return 해야할 경우 시작지점 저장을 위해 
        for(int num: nums){
            if(!set.contains(num -1)){ // to check only once. to avoid cyclic checking
                int currentSize = 1;
                int element = num + 1;
                while(set.contains(element)){
                    currentSize++;
                    element++;
                }
                //longestSize = math.Max(longestSize, currentSize);
                if(longestSize < currentSize){
                    startElement = num;
                    longestSize = currentSize;
                }
            }
        }

       
       // while(set.contains(startElement)){
        //    result.add(startElement);
        //    startElement++;
       // }
       // Integer[] resultArray1 = new Integer[result.size()]; //이방식은 int[] 는 안되네. 
       // result.toArray(resultArray1);
       // int[] resultArray = new int[result.size()];

       // for(int i = 0; i < resultArray.length; i++){
       //         resultArray[i] = result.get(i);
       //         System.out.print(resultArray[i] + " ");
       // }
       

        return longestSize;
    }
}


//Similar question: 
//  2274. Maximum Consecutive Floors Without Special Floors
//  298. Binary Tree Longest Consecutive Sequence

//2022.10.24
//Limitation : if nums is null or size is zero, return 0?

//input: nums = [100,4,200,1,3,2] -> output : 4
//input: nums = [0,3,7,2,5,8,4,6,0,1] -> output: 9

//Idea : Using HashSet (no sorting algorithm. )

//Time Complexity : O(n)
//Space Complexity: O(n)
/*
class Solution {
    public int longestConsecutive(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return 0;
        }
        
        //make HashSet to find some number with O(n) time complexity
        HashSet<Integer> numSet = new HashSet<>();
        for(int i = 0; i < nums.length; i++){
            numSet.add(nums[i]);
        }
        
        int longest = 1;
        //check the consecutive sequence
        for(int num : nums){

            if(!numSet.contains(num-1)){ //first number of some consecutive sequence
                int consecutive = 1;
                int next = num+1;
                while(numSet.contains(next)){
                    consecutive++;
                    next++;
                }
                
                longest = Math.max(consecutive, longest);
            }
        }
        
        return longest;
    }
}
*/