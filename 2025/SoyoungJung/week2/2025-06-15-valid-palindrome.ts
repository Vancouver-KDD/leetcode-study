function isPalindrome(s: string): boolean {
  const filtered = s
    .trim()
    .replace(/[^a-zA-Z0-9]/g, "")
    .toLowerCase();
  let left = 0;
  let right = filtered.length - 1;

  while (left <= right) {
    if (filtered[left] !== filtered[right]) return false;
    left++;
    right--;
  }

  return true;
}
