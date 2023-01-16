/**
 * @param {string[]} strs
 * @return {string[][]}
 */
var groupAnagrams = function(strs) {
    const hash = new Map();
    strs.forEach(str => {
        let letters = str.split('').sort();
        hash[letters] ? hash[letters].push(str) : hash[letters] = [str];
    })

    const keys = Object.keys(hash);
    const values = keys.map(value => hash[value]);
    return values;
};