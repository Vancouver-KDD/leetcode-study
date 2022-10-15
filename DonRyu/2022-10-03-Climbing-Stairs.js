var climbStairs = function (n) {
  if (n == 1 || n == 0) return 1 // our base cases

  let first = 1;
  let second = 2;

  for (let i = 3; i <= n; i++) {
    let third = first + second;
    first = second;
    second = third;
  }
  return second;

};

const climbStairs2 = (n) => {
  let one = 1;
  let two = 1;

  for (let i = 1; i < n; i++) {
    let tmp = one;
    one = one + two
    two = tmp
  }

  return one
}

console.log(climbStairs2(3))
