class Solution {
  /**
   * @param {string[]} strs
   * @return {string[][]}
   */
  groupAnagrams(strs) {
    const sortAlphabet = (word) => {
      return word.split("").sort().join("");
    };

    const strsObject = {};
    strs.forEach((str) => {
      const sortedWord = sortAlphabet(str);
      if (sortedWord in strsObject) {
        strsObject[sortedWord].push(str);
      } else {
        strsObject[sortedWord] = [str];
      }
    });

    return Object.values(strsObject);
  }
}
