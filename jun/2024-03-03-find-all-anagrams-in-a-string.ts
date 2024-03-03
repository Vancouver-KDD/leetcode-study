function findAnagrams(s: string, p: string): number[] {
    const result: number[] = []
    let start = 0,
        end = 0
    const map = new Map()
    const windowCounts = new Map()

    for (const char of p) {
        map.set(char, (map.get(char) || 0) + 1)
    }
    while (end < s.length) {
        windowCounts.set(s[end], (windowCounts.get(s[end]) || 0) + 1)
        if (end - start > p.length - 1) {
            windowCounts.set(s[start], windowCounts.get(s[start]) - 1)
            if (windowCounts.get(s[start]) === 0) {
                windowCounts.delete(s[start])
            }
            start++
        }
        console.log(`end: ${end}, start: ${start}`)
        if (end - start === p.length - 1 && isAnagram(map, windowCounts)) {
            result.push(start)
        }
        end++
    }
    return result
}

function isAnagram(map, windowCounts) {
    for (const [key, value] of map) {
        if (windowCounts.get(key) !== value) {
            return false
        }
    }
    return true
}
