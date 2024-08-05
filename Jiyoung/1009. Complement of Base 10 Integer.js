var bitwiseComplement = function (n) {
    if (n === 0) return 1;

    const bin = n.toString(2).split("").map(x => x === '1' ? '0' : '1').join("");
    return parseInt(bin, 2);
};
