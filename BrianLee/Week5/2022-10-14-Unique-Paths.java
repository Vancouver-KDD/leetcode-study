class Solution {
    public int uniquePaths(int x, int y) {
        return fun(0,0,x,y,new HashMap<>());
    }

    private int fun(int n, int m, int x, int y, Map<String,Integer> counts) {
        if(n == x-1 && m == y -1) return 1;
        if(counts.containsKey(n+","+m)) return counts.get(n+","+m);

        int count = 0;
        if(n+1 < x) count += fun(n+1, m, x, y, counts);
        if(m+1 < y) count += fun(n, m+1, x, y, counts);
        counts.put(n+","+m, count);

        return count;
    }
}