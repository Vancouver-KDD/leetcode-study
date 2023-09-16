/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var threeSumClosest = function (nums, target) {
    let l = nums.length;
    let closest = Number.MAX_SAFE_INTEGER;
    let res = 0;

    nums.sort((a,b)=>a-b);

    for (let i = 0; i < l - 2; i++) {
        let s = i + 1;
        let e = l - 1;
        while (s < e) {
            let r = nums[i] + nums[s] + nums[e];
            let o = Math.abs(r - target);

            if (r == target) {
                return r;
            }
            else if (r > target) {
                e--;
            }
            else {
                s++;
            }

            if (closest > o) {
                closest = o;
                res = r;
            }
        }
    }

    return res;
};