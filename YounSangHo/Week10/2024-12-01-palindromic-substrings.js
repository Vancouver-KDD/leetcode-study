class Solution {
  /**
   * @param {string} s
   * @return {number}
   */
  countSubstrings(s) {
    //
    // in first we need to make substring
    // 1 a  b   c
    // 2 b  c
    // 3 c
    // in second we need to look for palindromic
    // time complexcity : O(n^3)
    // space complexcity : O(1)
    let res = 0;
    for (let i = 0; i < s.length; i++) {
      for (let j = i; j < s.length; j++) {
        let l = i,
          r = j;
        while (l < r && s[l] === s[r]) {
          l++;
          r--;
        }
        res += l >= r ? 1 : 0;
      }
    }

    return res;
  }
}
