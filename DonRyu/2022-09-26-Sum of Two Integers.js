const getSum = function (a, b) {
  let carry = 0
  while (b !== 0) {
    carry = a & b
    a ^= b
    b = carry << 1
  }
  return a
}
