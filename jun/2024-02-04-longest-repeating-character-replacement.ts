function characterReplacement(s: string, k: number): number {
  const map = {}
  let l = 0
  let r = 0
  let maximumFrequency = 0
  let result
  while (r < s.length) {
    const char = s[r]
    map[char] ||= 0
    map[char]++
    const potentialResult = r + 1 - l
    maximumFrequency = Math.max(maximumFrequency, map[char])
    if (potentialResult - maximumFrequency <= k) {
      result = result > potentialResult ? result : potentialResult
    } else {
      map[s[l]]--
      l++
    }
    r++
  }
  return result
}
