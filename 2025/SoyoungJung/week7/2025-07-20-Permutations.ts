function permute(nums: number[]): number[][] {
  const result: number[][] = [];

  const backtrack = (path: number[], remaining: number[]) => {
    if (remaining.length === 0) {
      result.push(path);
      return;
    }

    for (let i = 0; i < remaining.length; i++) {
      const next = remaining.slice(0, i).concat(remaining.slice(i + 1));
      backtrack([...path, remaining[i]], next);
    }
  };

  backtrack([], nums);
  return result;
}
