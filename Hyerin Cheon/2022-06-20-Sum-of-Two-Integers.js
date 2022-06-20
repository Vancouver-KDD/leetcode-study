function getSum (a, b){
  let carry;

  while((a & b) !== 0){
    carry = (a & b) << 1;
    a = a ^ b;
    b = carry;
  }
  return a ^ b;
}