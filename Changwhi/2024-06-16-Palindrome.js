/**
 * @param {string} s
 * @return {boolean}
 */
var isPalindrome = function(s) {
    const isAlphanumeric = (c) => {return (c.toLowerCase() >= 'a' && c.toLowerCase() <= 'z') || c>= "0" && c<= "9"} 
    let left = 0
    let right = s.length - 1

    while(left < right) {
        if (!(isAlphanumeric(s.charAt(right)))) {
            right --;
            continue;
        }  
        if (!(isAlphanumeric(s.charAt(left)))) {
            left ++;
            continue;
        }
        if (s.charAt(left).toLowerCase() !== s.charAt(right).toLowerCase()) {
            return false
        }
        left++
        right--
    }
    return true
};