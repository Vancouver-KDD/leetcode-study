/**
 * @param {string} s
 * @param {number} k
 * @return {number}
 */

var longestSubstring = function (s, k) {

    if (s == null || s.length < k) {
        return 0;
    }

    if (k <= 1) {
        return s.length;
    }

    let maxUnique = new Set(s).size;
    let maxLen = 0;

    for (let i = 1; i <= maxUnique; i++) {
        const freq = new Map();
        let start = 0, currUnique = 0, countAtLeastK = 0;

        for (let end = 0; end < s.length; end++) {
            freq.set(s[end], (freq.get(s[end]) || 0) + 1);
            if (freq.get(s[end]) === k) countAtLeastK++;
            if (freq.get(s[end]) === 1) currUnique++;

            while (currUnique > i) {
                if (freq.get(s[start]) === k) countAtLeastK--;
                freq.set(s[start], freq.get(s[start]) - 1);
                if (!freq.get(s[start])) currUnique--;
                start++;
            }
            if (currUnique === countAtLeastK) {
                maxLen = Math.max(maxLen, end - start + 1);
            }
        }
    }
    return maxLen;
};
