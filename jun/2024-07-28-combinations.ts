function combine(n: number, k: number): number[][] {
    const result: number[][] = []
    function helper(curr: number, subset: number[]) {
        if (subset.length == k) {
            result.push(subset)
            result
        }
        for (let i = curr + 1; i <= n; i++) {
            if (i > curr) {
                helper(i, [...subset, i])
            }
        }
    }
    helper(0, [])
    return result
}
