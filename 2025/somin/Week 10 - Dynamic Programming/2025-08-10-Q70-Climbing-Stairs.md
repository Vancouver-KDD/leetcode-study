```
class Solution {
    public int climbStairs(int n) {
        if(n<=2) return n; //n=1 -> [1], n=2->[1+1, 2]  
        int a = 1; 
        int b = 2;
        int result =0;
        
        for(int i=3; i<=n; i++){
            result = a + b;
            a=b;
            b=result;
        }
        return result;
    }
}
```
