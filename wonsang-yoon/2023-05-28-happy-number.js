/**
 * @param {number} n
 * @return {boolean}
 */
var isHappy = function (n) {
    if (n < 0) {
        return false;
    }
    while (n) {
        let n_array = n.toString().split("");
        let first = Math.pow(n_array[0], 2);
        let second = Math.pow(n_array[1], 2);
        n = first + second
        if (n === 1) {
            return true
        }else if(n_array.length === 1 && n_array[0] !== 1){
            console.log(n_array[0])
            return false
        }
    }

};