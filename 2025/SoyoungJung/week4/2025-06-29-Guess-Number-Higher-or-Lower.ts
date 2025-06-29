const target = 42;

function guess(num: number): -1 | 0 | 1 {
  if (num === target) return 0;
  if (num > target) return -1;
  return 1;
}

function guessNumber(n: number): number {
  let low = 1;
  let high = n;

  while (low <= high) {
    const mid = Math.floor(low + (high - low) / 2);
    const result = guess(mid);

    if (result === 0) {
      return mid;
    } else if (result === -1) {
      high = mid - 1;
    } else {
      low = mid + 1;
    }
  }

  return -1;
}
