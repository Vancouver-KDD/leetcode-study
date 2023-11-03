//Dynamic programming - 0/1 Knapsack 문제 
// 2023-10-30

//풀이: idea1-> idea2 -> idea3 -> idea4-> idea 5 

//idea1 - Brute force - recursive call
//현재 index 의 value 선택하는 경우 , 선택하지 않는 경우를 recursive 하게 체크해나감. 
//각 index 별로 선택된경우 아닌경우에 대해 현재까지의 sum 을 구해서 그게 totalSum 의 절반이 된다면 반으로 나눌수 있는게 맞으니 return true, 아닌경우 false , 최종적으로 true 가 한번이라도 있으면 true 가 리턴됨. 
//Time Complexity: O(2^n) <--매 값마다 선택할경우/선택하지 않을경우 2가지 경우의수 체크
//Space Complexity: O(n) <-- recursive call stack 이 배열 사이즈만큼 
/*
class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length <= 0){
            return false;
        }
        
        int totalSum = 0; 
        for(int i = 0; i < nums.length; i++){
            totalSum += nums[i];
        }
        if(totalSum %2 != 0){ //cannot be partitioned in half
            return false;
        }
        totalSum = totalSum /2; 
        
        return recursiveCheck(nums, 0, totalSum);
    }
    
    boolean recursiveCheck(int[] nums, int index, int sum){
        if(sum == 0){
            return true;
        }
        if(index >= nums.length || sum < 0 ){
            return false;
        }
        
        return recursiveCheck(nums, index+1, sum - nums[index]) || recursiveCheck(nums, index+1, sum);
    }
}
*/

//idea2 - recursive call + memoizaion (MxN array table)
//idea1 의 경우를 보면 같은 값을 또 체크하는 경우가 생김, 이것을 table 에 저장 
//Time Complexity: O(MxN) , In the worst case where there is no overlapping calculation => MxN
//Space Complexity: O(MxN) , recursive call stack  O(N) + memoization O(MxN) => O(MxN)
/*
class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length <= 0){
            return false;
        }
        int totalSum = 0; 
        for(int i = 0; i < nums.length; i++){
            totalSum += nums[i];
        }
        if(totalSum %2 != 0){ //cannot be partitioned in half
            return false;
        }
        totalSum = totalSum /2; 
        
        Boolean[][] memo = new Boolean[nums.length][totalSum+1];
        
        return recursiveCheck(nums, memo, 0, totalSum);
    }
    
    boolean recursiveCheck(int[] nums, Boolean[][] memo, int index, int sum){
        if(sum == 0){
            return true;
        }
        if(index >= nums.length || sum < 0 ){
            return false;
        }
        if(memo[index][sum] != null){
            return memo[index][sum];
        }
        
        memo[index][sum] = recursiveCheck(nums, memo, index+1, sum - nums[index]) || recursiveCheck(nums, memo, index+1, sum);
        
        return memo[index][sum];
    }
}
*/
//idea3 - dynamic programming using memoizaion (MxN array table)
//idea2 memoization 이  recursive call 필요없이 iteration 으로 가능함. 
//Dynamic programming 식은 idea2 의 recursive call 로부터 얻어낼수 있음. 
//  - dp[i][j] = dp[i+1][j - nums[i]] || dp[i+1][j] (단 j - nums[i] >= 0)
//  - j - nums[i] < 0 인 경우는 return false 이기때문에 dp[i+1][j] 만 체크하면됨
//  - dp[i][j] = dp[i+1][j]  ( if, j - nums[i] < 0)
//  [Base Case]
//  - dp[i][0] = true  (sum 이 0 이면 true. we do not need to choose an element to for a subset whose sum is 0. )
//  - dp[nums.length][j] = false ( no element to choose)
// ==> 위 식을 통해 i+1 -> i 순으로 dynamic programming 

//Time Complexity: O(MxN) , We iteratively fill the array of size MxN.
//Space Complexity: O(MxN), memoization O(MxN)
/*
class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length <= 0){
            return false;
        }
        int totalSum = 0; 
        for(int i = 0; i < nums.length; i++){
            totalSum += nums[i];
        }
        if(totalSum %2 != 0){ //cannot be partitioned in half
            return false;
        }
        totalSum = totalSum /2; 
        
        boolean[][] dp = new boolean[nums.length +1][totalSum +1]; //Boolean object's default value is Null, boolean is primitive type. default value is false
        
        for(int i = 0; i <= nums.length; i++){
            dp[i][0] = true;
        }
        
        for(int i = nums.length -1; i >= 0; i--){
            for(int j= 1; j <= totalSum; j++){
                if(j - nums[i] >= 0){
                    dp[i][j] = dp[i+1][j - nums[i]] || dp[i+1][j];
                }else{
                    dp[i][j] = dp[i+1][j];
                }                
            }
        }
        return dp[0][totalSum]; //recursive call 에서 recursiveCheck(nums, 0, totalSum) 한것과 같은 결과
    }
}
*/

//idea4 - dynamic programming using memoizaion (2 X N array table)
//idea3 의 방법이 2 rows array 로 가능함. -> [i] 는 [i+1] row 의 값만 필요하기때문
//Dynamic programming 식은 idea2 의 recursive call 로부터 얻어낼수 있음. 
//  - dp[i][j] = dp[i+1][j - nums[i]] || dp[i+1][j] (단 j - nums[i] >= 0)
//  - j - nums[i] < 0 인 경우는 return false 이기때문에 dp[i+1][j] 만 체크하면됨
//  - dp[i][j] = dp[i+1][j]  ( if, j - nums[i] < 0)
//  [Base Case]
//  - dp[i][0] = true  (sum 이 0 이면 true. we do not need to choose an element to for a subset whose sum is 0. )
//  - dp[nums.length][j] = false ( no element to choose)
// ==> 위 식을 통해 i+1 -> i 순으로 dynamic programming 

//Time Complexity: O(MxN) , We iteratively calculate  MxN times.
//Space Complexity:  O(M) , memoization O(M *2) => O(M)
/*
class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length <= 0){
            return false;
        }
        int totalSum = 0; 
        for(int i = 0; i < nums.length; i++){
            totalSum += nums[i];
        }
        if(totalSum %2 != 0){ //cannot be partitioned in half
            return false;
        }
        totalSum = totalSum /2; 
        
        boolean[][] dp = new boolean[2][totalSum +1]; //Boolean object's default value is Null, boolean is primitive type. default value is false
        
        for(int i = 0; i < 2; i++){
            dp[i][0] = true;
        }
        
        for(int i = nums.length -1; i >= 0; i--){
            for(int j= 1; j <= totalSum; j++){
                if(j - nums[i] >= 0){
                    dp[i & 1][j] = dp[(i+1) & 1][j - nums[i]] || dp[(i+1) & 1][j];
                }else{
                    dp[i & 1][j] = dp[(i+1) & 1][j];
                }                
            }
        }
        return dp[0][totalSum]; //recursive call 에서 recursiveCheck(nums, 0, totalSum) 한것과 같은 결과        
    }
}
*/

//idea5 - dynamic programming using memoizaion (1 dimensional array table)
//idea4 의 방법이 1차원 array 로 가능함. (오른쪽에서 왼쪽으로 update 하는게 중요 => 왼쪽값을 참조해서 오른쪽이 update 되기 때문에 가능. )

//Dynamic programming 식은 idea2 의 recursive call 로부터 얻어낼수 있음. 
//  - dp[i][j] = dp[i+1][j - nums[i]] || dp[i+1][j] (단 j - nums[i] >= 0)
//  - j - nums[i] < 0 인 경우는 return false 이기때문에 dp[i+1][j] 만 체크하면됨
//  - dp[i][j] = dp[i+1][j]  ( if, j - nums[i] < 0)
//  [Base Case]
//  - dp[i][0] = true  (sum 이 0 이면 true. we do not need to choose an element to for a subset whose sum is 0. )
//  - dp[nums.length][j] = false ( no element to choose)
// ==> 위 식을 통해 i+1 -> i 순으로 dynamic programming 

//Time Complexity: O(MxN) , We iteratively calculate  MxN times.
//Space Complexity:  O(M) , memoization 길이가 M 인 1차원 array

class Solution {
    public boolean canPartition(int[] nums) {
        if(nums == null || nums.length <= 0){
            return false;
        }
        int totalSum = 0; 
        for(int i = 0; i < nums.length; i++){
            totalSum += nums[i];
        }
        if(totalSum %2 != 0){ //cannot be partitioned in half
            return false;
        }
        totalSum = totalSum /2; 
        
        boolean[] dp = new boolean[totalSum +1]; //Boolean object's default value is Null, boolean is primitive type. default value is false
        
        dp[0] = true;
        
    //dp[i][j] = dp[i+1][j - nums[i]] || dp[i+1][j] 식을 보면 [i]의 경우 [i+1] 만쓰고
    //[j]의 경우는 [j]자신 또는 더 작은 [j-nums[i]] 값만 사용함 = 즉 왼쪽의 값만 사용
    //이를 이용해서 오른쪽부터 update 해 나가면, 2줄 row 가 필요없이 1 row 만 있어도 됨. 
        for(int i = nums.length -1; i >= 0; i--){
            for(int j= totalSum; j > 0; j--){
                if(j - nums[i] >= 0){
                    dp[j] = dp[j - nums[i]] || dp[j];
                }
                //else{
                    //dp[j] = dp[j];  값 그대로 불변.
                //}                
            }
        }
        return dp[totalSum]; //recursive call 에서 recursiveCheck(nums, 0, totalSum) 한것과 같은 결과        
    }
}
