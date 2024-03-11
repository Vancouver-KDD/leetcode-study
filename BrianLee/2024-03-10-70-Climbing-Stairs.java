https://leetcode.com/problems/climbing-stairs/description/

class Solution {
    public int climbStairs(int n) {
        return climbMemStairs(n, new HashMap<>());
    }

    public int climbMemStairs(int n, Map<Integer, Integer> mem) {
        if(mem.containsKey(n)) return mem.get(n);
        if(n == 0) return 0;
        if(n == 1) return 1;
        if(n == 2) return 2;

        mem.put(n-1, climbMemStairs(n-1, mem));
        mem.put(n-2, climbMemStairs(n-2, mem));

        return mem.get(n-1) + mem.get(n-2);
    }
}