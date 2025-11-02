/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function (strs) {
  // we got array of strings
  // group the anagrams together

  // 1. 받은 배열을 반복문을이용해서 문자열을 받는다
  // 2. 문자열의 문자들을 알파뱃 순서로 바꾼다.
  // 3. 결과 배열에 있는지 확인후 없으면 하나의 그룹을 만들어 결과 배열에 넣고 있으면 이미있는 그룹에 넣는다.

  // if empty array then return strs
  if (strs.length === 0) {
    return strs;
  }

  let map = new Map();

  strs.forEach((str) => {
    const key = str.split("").sort().join("");
    if (!map.has(key)) map.set(key, []);
    map.get(key).push(str);
  });

  return Array.from(map.values());
};
