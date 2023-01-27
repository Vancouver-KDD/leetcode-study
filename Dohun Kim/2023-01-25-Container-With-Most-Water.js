/**
 * @param {number[]} height
 * @return {number}
 */
var maxArea = function(height) {
    let max = 0;
    let l = 0; // first element
    let r = height.length-1; // last element
    while (l < r) {
        max = Math.max(max, (r - l) * Math.min(height[l], height[r]));
        if (height[l] < height[r]) l++;
        else r--;
    }
    return max;
};