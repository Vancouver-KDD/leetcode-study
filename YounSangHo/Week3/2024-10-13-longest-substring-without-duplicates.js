class Solution {
  /**
   * @param {string} s
   * @return {number}
   */
  lengthOfLongestSubstring(s) {
    // 중복 되지 않는 단어 부분 문장을 찾아서 문장의 크기가 가장큰 크기를 출력해라
    // 1. the string change to a array
    // 2. 순차적으로 문자를 서브문장에 넣는다.
    // 3. 문자를 넣기전 서브문장에 해당 문자가 있는지 확인 있으면 문자를 포함한 앞부분을 제거한다.
    // 4. 서브문장의 크기를 확인하며 기존에 문장의 길이보다 큰경우 교체
    // zxyzxyz
    // z -> zx - zxy -> zxyz , xyz -> xyzx, yzx -> yzxy, zxy -> xyz
    let charArr = s.split("");
    let subStr = "";
    let maxLength = 0;

    for (let cha of charArr) {
      if (!subStr.includes(cha)) {
        subStr += cha;
      } else {
        subStr = subStr.slice(subStr.indexOf(cha));
      }

      maxLength = Math.max(maxLength, subStr.length);
      console.log(maxLength);
      console.log(subStr);
    }

    return maxLength;
  }
}
