// alternative fibonacci method
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

// fibonacci using for loop
class Solution {
public:
    int climbStairs(int n) {
        // number of methods depicts fibonacci
        // {1,2,3,5,8,13,...}
        
        if(n<0) return 0;
        
        int methods[n+1];
        methods[0]=1, methods[1]=1;
        
        for(int i=2; i<=n; i++){
            methods[i] = methods[i-1] + methods[i-2];
        }
        return methods[n];
    }
};

// fibonacci using recursion
// time limit exceeded
class Solution {
public:
    int climbStairs(int n) {
        // number of methods depicts fibonacci
        // {1,2,3,5,8,13,...}
        if(n<0) return 0;
        if(n==0 || n==1) return 1;
        return climbStairs(n-1)+climbStairs(n-2);
    }
};