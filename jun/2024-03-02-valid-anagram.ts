// 62ms
function isAnagram(s: string, t: string): boolean {
    const sLength = s.length
    const tLength = t.length
    const dict = new Map()
    if (sLength !== t.length) {
        return false
    }
    for (let i = 0; i < sLength; i++) {
        dict.set(s[i], (dict.get(s[i]) || 0) + 1)
    }
    for (let i = 0; i < tLength; i++) {
        const count = dict.get(t[i])
        if (count) {
            dict.set(t[i], count - 1)
        } else {
            return false
        }
    }
    return true
}

// 91ms
function isAnagram2(s: string, t: string): boolean {
    return s.split('').sort().join('') === t.split('').sort().join('')
}
