function climbStairs(n: number): number {
  if (n <= 2) return n;

  let prev2 = 1,
    prev1 = 2;
  for (let i = 3; i <= n; i++) {
    const temp = prev1;
    prev1 = prev1 + prev2;
    prev2 = temp;
  }
  return prev1;
}
