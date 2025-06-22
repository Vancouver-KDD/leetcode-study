class Solution {
  constructor() {
    this.memo = {};
  }
  /**
   * @param {string} s
   * @param {string[]} wordDict
   * @return {boolean}
   */
  wordBreak(s, wordDict) {
    const stringLength = s.length;

    const dfs = (currentStr) => {
      let res = false;
      if (currentStr.length > stringLength) {
        return false;
      } else if (currentStr == s) {
        return true;
      }

      console.log(currentStr);

      wordDict.forEach((word) => {
        if (dfs(currentStr + word)) {
          res = true;
        }
      });

      return res;
    };

    return dfs("");
  }
}
