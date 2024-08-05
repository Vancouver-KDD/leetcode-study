//brute-force
var singleNumber = function (nums) {
    let map = new Map();
    let result = -1;

    for (i of nums) {
        if (map.has(i)) {
            map.set(i, map.get(i) + 1);
        } else {
            map.set(i, 1);
        }
    }

    map.forEach((value, key, map) => {
        if (value === 1) result = key;
    })

    return result;
};
