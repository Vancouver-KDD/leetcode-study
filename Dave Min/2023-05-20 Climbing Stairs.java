
public class Solution {
    int[] visited = new int[50];
    public int ClimbStairs(int n) {
        if(n < 2) return 1;
        if(visited[n] != 0) return visited[n];
        var num =  ClimbStairs(n-1) + ClimbStairs(n-2);
        if(visited[n] == 0) visited[n] = num;
        return num;
    }
}

//1 2 3 5 8 

// 1 1 -->  1
// 2 11 2 --> 2
// 3 111 12 21 --> 3
// 4 1111 22 121 112 211  --> 5

//TC = O(2^n)
//SC = O(N)
