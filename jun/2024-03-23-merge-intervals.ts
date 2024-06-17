function merge(intervals: number[][]): number[][] {
    intervals.sort((a, b) => a[0] - b[0])
    const result = [intervals[0]]
    for (let i = 1; i < intervals.length; i++) {
        const lastInterval = result[result.length - 1]
        const [start, end] = intervals[i]
        if (lastInterval[1] >= start) {
            lastInterval[1] = Math.max(lastInterval[1], end)
        } else {
            result.push(intervals[i])
        }
    }
    return result
}
