
// limitation: the array is sorted??? no?? 
//              if nums is null or size is 0, return null
// Input: nums = [-1,0,1,2,-1,-4] , Output: [[-1,-1,2],[-1,0,1]]
// Input: nums = [-1,0,1,2,-1,-1, -1 ,-4] , Output: [[-1,-1,2],[-1,0,1]]

// Input: nums = [0,1,1] , Output: []
//2023-01-21 --[2]
//Time Complexity: O(N^2)
//Space Complexity: from O(log⁡n) to O(n), depending on the implementation of the sorting algorithm. For the purpose of complexity analysis, we ignore the memory required for the output.
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> sumList = new ArrayList<>();
        if(nums == null || nums.length == 0){
            return sumList;
        }
        //Sort to avoid the duplicate triples
        Arrays.sort(nums);

        for(int first = 0; first < nums.length; first++){
            if((first > 0) && (nums[first] == nums[first-1])){
                continue; //skip this number
            }

            int second = first +1; 
            int third = nums.length -1;
            while(second < third){
                int sum = nums[first] + nums[second] + nums[third];
                if(sum == 0){
                    List<Integer> list = Arrays.asList(nums[first], nums[second], nums[third]);
                    sumList.add(list);
                    second++;
                    third--;
                }else if(sum < 0){
                    second++; //to increase sum
                }else{
                    third--; //to reduce sum
                }

                //to avoid the duplicate
                while((second > (first+1)) && (second < third) && nums[second] == nums[second -1]){
                        second++;
                }
                while((second < third) && (third < (nums.length-1)) && nums[third] == nums[third+1]){
                        third--;
                }
            }
        }

        return sumList;
    }
}

//2023-01-21 --[1]--- 아래 방법으로 하니 Time Limit Exceeded 가 나네
//[idea] - two sum 을 구하고, 그다음 나머지 하나를 찾는건데... 같은 숫자가 나오면 건너뛰게 하는게 관건
//Time Complexity: O(N^3)
//Space Complexity: O(N) <--- return 할 메모리??
/*
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> sumList = new ArrayList<List<Integer>>();
        if(nums == null || nums.length == 0){
            return sumList;
        }
        //Sort to avoid the duplicate triples
        Arrays.sort(nums);

        int first, second, third;
        first = 0;
        while(first < nums.length){
            while((first > 0) && (first < nums.length) && (nums[first]== nums[first-1])){ //to avoid the duplicate
                first++;
            }
            second = first +1;
            while(second < nums.length){
                while((second > (first+1)) && (second < nums.length) && (nums[second] == nums[second-1])){
                    second++;
                }
                third = second + 1;
                while(third < nums.length){
                    int sum = nums[first] + nums[second] + nums[third];
                    if(sum == 0){
                        List<Integer> list = Arrays.asList(nums[first], nums[second], nums[third]);
                        sumList.add(list);
                        break;
                    }else{
                        third++;
                    }
                }
                second++;
            }
            first++;
        }
        return sumList;
    }
}
*/

//2022.12.01
//Time Complexity: O(N^2)
//Space Complexity: O(N)
/*
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        List<List<Integer>> result = new ArrayList<>();

        if(nums == null){
            return result;
        }

        //To avoid duplicated case, 
        Arrays.sort(nums); 

        for(int i = 0; i < nums.length ; i++){
            if(i >0 && nums[i] == nums[i-1]){
                continue;
            }
            int start = i+1; 
            int end = nums.length -1;
            while(start < end){
                int sum = nums[i] + nums[start] + nums[end];
                if(sum == 0){
                    List<Integer> zeroList = Arrays.asList(nums[i], nums[start], nums[end]);
                    result.add(zeroList);
                    start++;
                    end--;
                    //to remove duplicated case
                    while(start < end && nums[end] == nums[end+1]){
                        end--;
                    }
                    while(start < end && nums[start] == nums[start-1]){
                        start++;
                    }
                }else if( sum > 0){
                    end--; // to reduce sum.
                }else{ //sum < 0
                    start++; // to increase sum
                }
            }
        }
        return result;
    }
}
*/
//Time Complexity: O(n^2)    
// Space Complexity: O(n) <---  Sorting 하는데 든 메모리라고 하네  (java 는 array sort 를 위해 quicksort 를 쓰는데 time complexity: O(nlogn) , space complexity: O(n) , 사실 time complexity 도 quick sort 의 worst case 는 O(n^2) 인데 java 에서는 개선된 것을 써서 n^2 가 발생하지 않고 worst case 가 nlogn 되게 해준다고 함. )
//2022.09.25
/*
class Solution{
    public List<List<Integer>> threeSum(int[] nums){
        
        List<List<Integer>> threeSumList = new ArrayList<>();
        
        if(nums == null || nums.length == 0){
            return threeSumList;
        }
        
        //To avoid duplicated cases
        Arrays.sort(nums);
        
        //-4, -1, -1, 0, 1, 2
        
        for(int i = 0; i < nums.length; i++){
            
            if((i>0) && (nums[i] == nums[i-1])){
                //To avoid the duplicated cases, skip it
                continue; 
            }
            
            int start = i+1;
            int end = nums.length -1; 
            while(start < end){
                int sum = nums[i] + nums[start] + nums[end];
                if(sum == 0){
                    List<Integer> eachList = Arrays.asList(nums[i], nums[start], nums[end]);
                    threeSumList.add(eachList);
                    
                    start++;
                    end--;
                    
                    //To avoid duplicated cases
                    while((start < end) && (nums[start] == nums[start-1])){
                        start++;
                    }
                    while((start < end) && (nums[end] == nums[end+1])){
                        end--;
                    }
                    
                    
                }else if(sum > 0){
                    end--;
                }else{// sum < 0
                    start++;
                }
            }
        }
        
        return threeSumList;
    }
}
*/
//2022.09.21
/*
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
*/
//2022.09.04
/*
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        if(nums == null || nums.length < 3){
            return null;
        }
        
        Arrays.sort(nums);
        
        List<List<Integer>> tripletList = new ArrayList<List<Integer>>();
        
        int length = nums.length; 
        for(int i = 0; i < (nums.length-2); i++ ){
            
            if(i != 0 && nums[i] == nums[i-1]){ // duplicate case skip
                continue;
            }
            
            int sum = nums[i] * -1;
            
            int low = i+1;
            int high = nums.length-1;
            while(low < high){
                int tempSum = nums[low] + nums[high];
                if(tempSum == sum){
                    List<Integer> triplet = Arrays.asList(nums[i], nums[low], nums[high]);
                    tripletList.add(triplet);
                    
                    low++;
                    while( (low <= (length -1)) && (nums[low-1] == nums[low])){
                        low++;
                    }
                    high--;
                    while((high > (i+1)) && (nums[high] == nums[high+1])){//이건 필요없나?
                        high--;
                    }
                    
                }else if(tempSum > sum){
                    high--;
                }else{//tempSum < sum
                    low++;
                }
                
            }
        } 
        
        return tripletList;
        
    }
}
*/
//아래 솔루션은 triplet 세트는 구했으나 그 세트내에서 duplicate 이 존재함. 
//ex. Input: nums = [-1,0,1,2,-1,-4],  output: [[-1,1,0],[-1,-1,2],[0,1,-1],[1,0,-1],[2,-1,-1]]
/*
class Solution {
    public List<List<Integer>> threeSum(int[] nums) {
        
        if(nums == null || nums.length == 0){
            return null;
        }
        
        int length = nums.length;
        List<List<Integer>> tripletList = new ArrayList<List<Integer>>();
        
        
        HashSet<Integer> threeSumMap = new HashSet<Integer>();
        HashMap<Integer, Integer> twoSumMap;
        
        //make first map.  HashMap(Key: needed Sum, value: index)
        for(int i = 0; i < length; i++){
            int neededSum = nums[i] * -1;
            
            
            //if it is not duplicated
            if(!threeSumMap.contains(neededSum)){ // hashset 으로 바꾸자.... 
                threeSumMap.add(neededSum);
                //System.out.println("["+i+"]:"+nums[i]+"_neededSum:" + neededSum);
                //create new list
                twoSumMap = new HashMap<Integer, Integer>();
                for(int j = 0; j < length; j++){
                    if(i != j){
                        int secondNum = nums[j];
                        
                        //System.out.println("["+i+"]:"+nums[i]+"_neededSum:" + neededSum + ", j["+j+"]:" + nums[j]+" neededNum=" + neededNum);
                        
                        if(twoSumMap.containsKey(secondNum)){
                            int thirdIndex = twoSumMap.get(secondNum);
                            if(thirdIndex != i){
                                List<Integer> triplet = Arrays.asList(nums[i], nums[j], nums[thirdIndex]);
                                tripletList.add(triplet); 
                            }
                        }else{
                            int neededNum = neededSum - secondNum;
                            twoSumMap.put(neededNum, j);
                        }
                            
                    }
                }
            }
        }
        
        return tripletList;
        
    }
}
*/