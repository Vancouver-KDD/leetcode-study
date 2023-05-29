/**
 * @param {number} n - a positive integer
 * @return {number}
 */
var hammingWeight = function (n) {
    // if(n.length !== 32){
    //     return false;
    // }
    let count = 0;
    while(n){
        if(n&1) count ++;
        n = n >>> 1
    }
    return count
};