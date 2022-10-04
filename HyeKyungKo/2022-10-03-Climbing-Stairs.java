//n > = 1

//Input: n = 2 ===> Output: 2
//Input: n = 3 ===> Output: 3

//2022-10-03
//Time Complexity: O(N) , Space complexity: O(1)

class Solution{
    public int climbStairs(int n){
                
        if(n <=0){
            return 0;
        }

        //f(0) =0, f(1) = 1, f(2) = 2
        //f(n) = f(n-1) + f(n-2)
        
        if(n <=2){
            return n;
        }
        
        int prePrev = 1;  // start with f(1)
        int prev = 2; // start with f(2)
        int numWays = 0;
        
        for(int i = 3;  i <= n; i++){
            numWays = prev + prePrev;
            prePrev = prev;
            prev = numWays;
        }
            
        return numWays;
    }
}
