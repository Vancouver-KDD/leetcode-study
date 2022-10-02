const countBits = function(n) {
    let output = [];

    // 0 index will be always 0
    output[0] = 0;

    for (i = 1; i <= n; i++) {
        output[i] = output[Math.floor(i / 2)] + i % 2;
    }
    return output;
}