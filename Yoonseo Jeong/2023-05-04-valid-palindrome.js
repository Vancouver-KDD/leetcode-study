/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    // check if parameter is valid
    if (!s || s.length < 1) {
        return false
    }

    // using JavaScript Methods make given string to lowercase and remove all non-alphanumeric characters
    // and compare to another string that has been reversed
    return s.toLowerCase().replace(/[^a-z0-9]/g, '') === s.toLowerCase().replace(/[^a-z0-9]/g, '').split("").reverse().join("") ? true : false

    // simple solution using JavaScript methods
    // complexity
    // time: O(n)
    // space: O(1)
};

var isPalindrome2 = function(s) {
    // check if parameter is valid
    if (!s || s.length < 1) {
        return false
    }

    // using JavaScript Methods make given string to lowercase and remove all non-alphanumeric characters
    s.toLowerCase().replace(/[^a-z0-9]/g, '')

    let first = 0
    let last = s.length - 1
    // using two index from start and end, compare them till they meet in the middle
    while (first < last) {
        if (s[first] !== s[last]) return false
        first++
        last--
    }
    return true
    
    // more space efficient than first solution since it will only loop O(n/2) 
    // after making string to lowercase and remove all non-alphanumeric characters
    // complexity
    // time: O(n)
    // space: O(n)
};