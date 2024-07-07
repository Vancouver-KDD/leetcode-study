var threeSum = function (nums) {
    let result = [];
    nums.sort((x, y) => x - y);
    const len = nums.length;

    if (len < 3) return result;
    if (nums[0] > 0) return result;

    let hashmap = new Map();
    for (let i = 0; i < len; i++) {
        hashmap.set(nums[i], i);
    }

    for (let i = 0; i < len - 2; i++) {
        for (let j = i + 1; j < len - 1; j++) {
            const numK = -1 * (nums[i] + nums[j]);
            if (hashmap.has(numK) && hashmap.get(numK) > j)
                result.push([nums[i], nums[j], numK]);
            j = hashmap.get(nums[j])
        }
        i = hashmap.get(nums[i])
    }

    return result;
};
