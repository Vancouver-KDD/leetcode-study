// 1. using shift
function reverseBits(n) {
  let result = 0;
  for(let i = 0; i < 32; i++){
    result += n & 1;
    n >>= 1;
    if(i < 31){
      result <<= 1;
    }
  }
  return result >>> 0;    // why...?
}

// 2. js one line
function reverseBits2(n){
  return Number.parseInt(n.toString(2).split('').reverse().join('').padEnd(32, "0"), 2);
}