class Solution {
public:
    int climbStairs(int n) {
        // number of methods depicts fibonacci
        // {1,2,3,5,8,13,...}

        if(n<0) return 0;
        if(n==0||n==1) return 1;
        if(n==2) return 2;
        
        int a=1, b=1, i=2, temp=0;
        while(i<n){
            a+=b;
            temp=b;
            swap(a,b);
            a=temp;
            i++;
        }
        return a+b;
    }
};