/**
 * Non-ASCII Delimiter
 * @param {string[]} strs
 * @return {string}
 */
const encode = (strs, nonASCIICode = String.fromCharCode(257)) => {
    return strs.join(nonASCIICode);/* Time O(N) | Ignore Auxillary Space O(N) */
};

/**
 * Non-ASCII Delimiter
 * @param {string[]} strs
 * @return {string}
 */
const decode = (strs, nonASCIICode = String.fromCharCode(257)) => {
    return strs.split(nonASCIICode);/* Time O(N) | Ignore Auxillary Space O(N) */
};