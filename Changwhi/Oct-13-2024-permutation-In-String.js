/**
 * @param {string} s1
 * @param {string} s2
 * @return {boolean}
 */
var checkInclusion = function(s1, s2) {
    if (s1.length > s2.length) {
        return false;
    }

    const s1Chars = Object.create(null);
    const s2Chars = Object.create(null);

    for (const ch of s1) {
        if (!(ch in s1Chars)) {
            s1Chars[ch] = 0;
            s2Chars[ch] = 0;
        }
        ++s1Chars[ch];
    }

    for (let i = 0; i < s1.length; ++i) {
        const ch = s2[i];
        if (ch in s1Chars) {
            ++s2Chars[ch];
        }
    }

    let matches = 0;
    let matched = 0;

    for (const ch in s1Chars) {
        if (s1Chars[ch] === s2Chars[ch]) {
            ++matches;
        }
        ++matched;
    }

    const last = s2.length - s1.length;

    for (let i = 0; i < last; ++i) {
        if (matches === matched) {
            return true;
        }

        const ch1 = s2[i];
        const ch2 = s2[i + s1.length];

        if (ch1 in s1Chars) {
            if (s1Chars[ch1] === s2Chars[ch1]) {
                --matches;
            } 
            s2Chars[ch1]--
            if (s1Chars[ch1] === s2Chars[ch1]) {
                ++matches;
            }
        }

        if (ch2 in s1Chars) {
            if (s1Chars[ch2] === s2Chars[ch2]) {
                --matches;
            } 
            s2Chars[ch2]++
            if (s1Chars[ch2] === s2Chars[ch2]) {
                ++matches;
            }
        }
    }

    return matches === matched;
};