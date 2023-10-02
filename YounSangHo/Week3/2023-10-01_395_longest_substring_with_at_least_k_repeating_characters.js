/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */
var longestSubstring = function(s, k) {
  // 문자열 길이가 k 미만이면 조건을 만족하는 부분 문자열이 없음
  if (s.length < k) {
      return 0;
  }
  
  // 각 문자의 빈도수를 저장할 객체를 생성합니다.
  const charCount = {};

  // 문자열의 모든 문자에 대해 빈도수를 계산합니다.
  for (const char of s) {
      charCount[char] = (charCount[char] || 0) + 1;
  }

  // 주어진 문자열이 모든 문자의 빈도수가 k 이상인 경우, 문자열의 길이를 반환합니다.
  if (Object.values(charCount).every(count => count >= k)) {
      return s.length;
  }

  // 아닌 경우, 문자열을 분할하여 가장 긴 부분 문자열을 찾습니다.
  let maxSubstrLength = 0;
  let start = 0;

  for (let end = 0; end < s.length; end++) {
      if (charCount[s[end]] < k) {
          maxSubstrLength = Math.max(maxSubstrLength, longestSubstring(s.slice(start, end), k));
          start = end + 1;
      }
  }

  // 마지막 부분 문자열도 검사합니다.
  maxSubstrLength = Math.max(maxSubstrLength, longestSubstring(s.slice(start), k));

  return maxSubstrLength;
};