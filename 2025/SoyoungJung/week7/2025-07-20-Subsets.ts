function subsets(nums: number[]): number[][] {
  const result: number[][] = [];
  nums.sort((a, b) => a - b);

  const backtrack = (start: number, path: number[]) => {
    result.push([...path]);

    for (let i = start; i < nums.length; i++) {
      path.push(nums[i]);
      backtrack(i + 1, path);
      path.pop();
    }
  };

  backtrack(0, []);
  return result;
}
