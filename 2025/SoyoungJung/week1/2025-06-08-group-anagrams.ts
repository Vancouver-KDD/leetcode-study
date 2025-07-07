function groupAnagrams(strs: string[]): string[][] {
  const result: { [key: string]: string[] } = {};

  for (const word of strs) {
    const sorted = word.split("").sort().join("");
    if (!result[sorted]) {
      result[sorted] = [];
    }
    result[sorted].push(word);
  }

  return Object.values(result).sort();
}
