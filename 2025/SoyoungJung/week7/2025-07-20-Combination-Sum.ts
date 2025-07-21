function combinationSum(candidates: number[], target: number): number[][] {
  const result: number[][] = [];

  function backtrack(remaining: number, start: number, path: number[]): void {
    if (remaining === 0) {
      result.push([...path]);
      return;
    }

    if (remaining < 0) return;

    for (let i = start; i < candidates.length; i++) {
      const current = candidates[i];
      path.push(current);
      backtrack(remaining - current, i, path);
      path.pop();
    }
  }

  backtrack(target, 0, []);
  return result;
}
