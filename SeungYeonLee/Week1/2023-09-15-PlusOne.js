/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    let length = digits.length;
    digits[length - 1] += 1;

    for (let i = length - 1; i > 0; i--) {
        if(digits[i] == 10){
            digits[i] = 0;
            digits[i-1] += 1;
        }
    }

    if(digits[0] == 10){
        let res = [];
        res.push(1);
        res.push(0);
        for(let i = 1; i < length; i++){
            res.push(digits[i]);
        }
        return res;
    }

    return digits;
};