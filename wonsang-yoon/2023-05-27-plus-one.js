/**
 * @param {number[]} digits
 * @return {number[]}
 */
var plusOne = function (digits) {
    let is10 = digits[digits.length - 1] + 1;
    console.log(is10);

    if (is10 === 10) {
        let index = digits.indexOf(digits[digits.length - 1]);

        digits.splice(index, 1)
        digits.splice(index, 0, '1');

        digits.splice(index + 1, 0, '0');
    } else {
        let index = digits.indexOf(digits[digits.length - 1]);
        digits.splice(index, 1)
        digits.splice(index, 0, is10);


    }
    return digits;
};