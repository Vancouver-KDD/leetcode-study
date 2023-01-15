/**
 * @param {string} s
 * @param {string} t
 * @return {boolean}
 */
var isAnagram = function(s, t) {
    if (s.length != t.length) return false;
    
    var hashMap = {};
    for (var i=0; i<s.length; i++) {
        if (!hashMap[s[i]]) {
            hashMap[s[i]] = 0;
        }
        hashMap[s[i]]++;
    }

    for (var j=0; j<t.length; j++) {
        if (!hashMap[t[j]]) {
            return false;
        }
        hashMap[t[j]]--;
    }
    return true;
};