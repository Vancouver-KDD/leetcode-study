function groupAnagrams(strs: string[]): string[][] {
    if (strs.length === 1) {
        return [strs]
    }
    const map = new Map()

    strs.forEach((str) => {
        const key = str.split('').sort().join('')
        map.set(key, [...(map.get(key) || []), str])
    })
    return [...map.values()]
}
