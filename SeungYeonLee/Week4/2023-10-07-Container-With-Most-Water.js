/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function (height) {
    let l = height.length;
    let start = 0;
    let end = l - 1;

    let result = 0;

    while (start < end) {

        let shorter;
        let sum;

        shorter = Math.min(height[start], height[end]);

        sum = shorter * (end - start);
        result = Math.max(sum, result);

        if (height[start] >= height[end]) {
            end--;
        } else {
            start++;
        }
    }

    return result;

};