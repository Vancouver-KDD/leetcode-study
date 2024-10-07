class Solution {
  /**
   * @param {string[]} strs
   * @returns {string}
   */
  encode(strs) {
    if (strs.length === 0) return "";

    strs = strs.map((str) => {
      return `${str.length}#${str}`;
    });

    const encodeStrs = strs.join("");

    return encodeStrs;
  }

  /**
   * @param {string} str
   * @returns {string[]}
   */
  decode(str) {
    let result = [];
    let i = 0;
    let length = "";
    while (i < str.length) {
      if (str[i] !== "#") {
        length += str[i];
        i++;
      } else {
        let strLength = parseInt(length, 10);
        i++;
        result.push(str.substring(i, i + strLength));
        i = i + strLength;
        length = "";
      }
    }

    return result;
  }
}
