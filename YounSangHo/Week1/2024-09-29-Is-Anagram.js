class Solution {
  /**
   * @param {string} s
   * @param {string} t
   * @return {boolean}
   */
  isAnagram(s, t) {
    if (s.length !== t.length) return false;

    let sArr = s.split("");
    let tArr = t.split("");
    const checkMap = new Map();
    let result = true;

    sArr.forEach((chr) => {
      if (checkMap.has(chr)) {
        checkMap.set(chr, checkMap.get(chr) + 1);
      } else {
        checkMap.set(chr, 1);
      }
    });

    tArr.forEach((chr) => {
      if (checkMap.has(chr)) {
        if (checkMap.get(chr) === 1) {
          checkMap.delete(chr);
        } else {
          checkMap.set(chr, checkMap.get(chr) - 1);
        }
      } else {
        result = false;
      }
    });

    return result && checkMap.size === 0;
  }
}
