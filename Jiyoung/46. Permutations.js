var permute = function (nums) {
    if (nums.length === 1) {
        return [nums];
    }

    let result = [];
    for (let i = 0; i < nums.length; i++) {
        const n = nums.shift();
        const perm = permute([...nums]);
        for (const p of perm) {
            p.push(n)
        }

        result.push(...perm);
        nums.push(n);
    }

    return result;
};
