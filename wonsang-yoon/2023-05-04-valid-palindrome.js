var isPalindrome = function (s) {
    //boundary check
    if(s.length < 1)
        return false;
    //pick valid characters only (number and alphabet)
    let filtered = s.replace(/[^a-zA-Z0-9]/g, "").toLowerCase();
    //if the string has empty string it's a palindrome
    if (filtered.length === 0)
        return true;
    /*  Logic: iterate beginning and ending alphabet together
        will try matching the start point and end point character
        if it does not match fail
    */
    for (let start = 0,last = filtered.length - 1; start < filtered.length; start++, last --) {
        //made two condition one is for odd and even number
        //odd will have same index at the end and even number will have 1 number difference
        if (start === last || (filtered.length % 2 === 0 && start - last === 1))
            return true;
        if (filtered[start] !== filtered[last])
            return false;
    }

};