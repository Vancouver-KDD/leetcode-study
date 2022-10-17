class Solution {
    public int numDecodings(String s) {
        return backtracking(s, 0, new int[s.length()]);

    }

    private int backtracking(String s, int cur, int[] mem) {
        if(cur == s.length()) return 1;
        if(mem[cur] != 0) return mem[cur];

        char c = s.charAt(cur);
        int count = 0;
        if(c != '0') {
            count = backtracking(s, cur+1, mem);
            if(cur+1 < s.length() && Integer.parseInt(c+""+s.charAt(cur+1)) <= 26) {
                count += backtracking(s, cur+2, mem);
            }
        } else {
            return 0;
        }
        return mem[cur] = count;
    }
}