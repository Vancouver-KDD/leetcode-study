// 모르겠다.


const countBits = function (n) {
    n++;                                             // now n is n+1 ##

    let nums = [0];
    while (nums.length < n) {
        nums = [
            ...nums,                                 // same
            ...nums.map((num) => num + 1),           // same but next numbers
        ];
    }
    nums.length = n;                                 // we only want 1st n+1 (see above ##) numbers, delete rest
    return nums;
};
