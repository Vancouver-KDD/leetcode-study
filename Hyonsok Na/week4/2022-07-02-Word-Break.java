class Solution 
{
  public boolean wordBreak(String s, List<String> wordDict )
  {
      // O(n^3) time | O(n) space
      if(s == null || s.length() == 0) return false;

      int n = s.length();

      // dp[i] represents whether s[0...i] can be formed by dict
      boolean[] dp = new boolean[n];
      HashSet<String> mySet = new HashSet<>(wordDict);

      for (int i = 0; i < n; i++) 
      {
          for (int j = 0; j <= i; j++) 
          {
              String sub = s.substring(j, i + 1);
    
              if(mySet.contains(sub) && (j == 0 || dp[j - 1])) 
              {
                  dp[i] = true;
                  break;
              }
          }
      }
      return dp[n - 1];
  }
}