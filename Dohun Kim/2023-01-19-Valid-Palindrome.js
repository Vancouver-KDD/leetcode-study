/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    if (!s.length)
        return true;
    const alphaNumeric = filterAlphaNumeric(s);
    return alphaNumeric === alphaNumeric.split('').reverse().join('');
};

const filterAlphaNumeric = (s, nonAlphaNumeric = new RegExp('[^a-z0-9]','gi')) => s
    .toLowerCase()
    .replace(nonAlphaNumeric, '')