/**
 * @param {string} s
 * @param {string[]} wordDict
 * @return {boolean}
 */
var wordBreak = function (s, wordDict) {
  // s문장에서 i포지션을 이동 해가면서 start부터 i사이에 있는 문자로 wordDict에 있는 단어를 만들 수 있는지 확인
  // 단어가 있는 경우 단어가 있엇던 곳에 True를 넣고 다시 확인
  // s문장 마지막을 확알할때 그 값이 T면 wordDict를 이용해서 s문장을 만들 수 있는것
  let dp = new Array(s.length + 1).fill(false);
  dp[0] = true;

  for (let i = 1; i <= s.length; i++) {
    for (let w of wordDict) {
      let start = i - w.length;
      if (start >= 0 && dp[start] && s.substring(start, i) === w) {
        dp[i] = true;
        break;
      }
    }
  }
  return dp[s.length];
};
