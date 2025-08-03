function findContentChildren(g: number[], s: number[]): number {
  g.sort((a, b) => a - b);
  s.sort((a, b) => a - b);
  let childIndex = 0;
  let cookieIndex = 0;

  while (childIndex <= g.length && cookieIndex <= s.length) {
    if (g[childIndex] <= s[cookieIndex]) {
      childIndex++;
    }
    cookieIndex++;
  }

  return childIndex;
}
