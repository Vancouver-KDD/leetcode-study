var groupAnagrams = function(strs) {
    if(strs.length === 1){
		return [strs]
	}
    const map = new Map()
    for(str of strs) {
        const key = str.split('').sort().join()
        map.set(key, [...(map.get(key) || []), str])
    }
    return [...map.values()]
};