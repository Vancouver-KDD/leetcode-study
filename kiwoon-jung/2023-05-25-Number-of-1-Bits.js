var hammingWeight = function (n) {
  let countOf1 = 0;
  let arrOfN = n.toString(2).split("");
  for (i = 0; i < arrOfN.length; i++) {
    if (arrOfN[i] === "1") {
      countOf1++;
    }
  }
  return countOf1;
};
