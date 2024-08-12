var topKFrequent = function(nums, k) {
    let map = new Map();
    for (const num of nums) {
        //map.set(num, (map.get(num) || 0) + 1);
        if (map.has(num)){
            map.set(num, map.get(num)+1);
        } else {
            map.set(num, 1);
        }
    }

    const sortedByValue = [...map.entries()].sort((a, b) => b[1] - a[1]);
    
    return sortedByValue.slice(0, k).map(entry => entry[0]);
};
