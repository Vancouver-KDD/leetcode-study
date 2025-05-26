class Solution {
  /**
   * @param {string} s
   * @param {number} k
   * @return {number}
   */
  characterReplacement(s, k) {
    //영어 대문자로 된 문장 k와 정수를 받음
    // 너는 k갯수의 단어들을(s문장에서 제공된) 선택할 수 있다
    // 그리고 그 단어들을 다른 단어들로 교체 할 수 있다.
    // k개의 단어를 교체하여 하나의 문자로 된 가장 긴 문장을 길이를 출력하라
    // XYYXYYYX, 1
    // X, XY 2 -> Y,XYY 3 -> Y, YYX 3 -> Y YYXY 4 -> Y YYXYY 5 -> Y YYXYYY 6 -> Y YYYX 4
    // 1. 기준이 되는 단어를 설정 첫번째 단어
    // 2. s를 반복문으로 돌리면서

    let strArr = s.split("");
    let primaryChar = strArr[0];
    let subStr = primaryChar;
    let diffCharCount = 0;
    let maxLength = 0;
    const maxCount = k;

    for (let i = 1; i < strArr.length; i++) {
      if (primaryChar === strArr[i]) {
        subStr += strArr[i];
      } else {
        diffCharCount++;
        if (diffCharCount <= maxCount) {
          subStr += strArr[i];
        } else {
          subStr += strArr[i];

          while (diffCharCount > maxCount) {
            primaryChar = subStr.charAt(subStr.length > 1 ? 1 : 0);
            diffCharCount = 0;
            for (let char of subStr.split("")) {
              if (primaryChar !== char) diffCharCount++;
            }
            if (diffCharCount > maxCount) {
              subStr = subStr.slice(1);
            }
          }
        }
      }
      maxLength = Math.max(maxLength, subStr.length);
    }

    return maxLength;
  }
}
