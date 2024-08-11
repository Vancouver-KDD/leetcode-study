var topKFrequent = function(words, k) {
    const wordMap = new Map();
    for (const word of words){
        wordMap.set(word, (wordMap.get(word) || 0) +1)
    }

    const sortedValue = [...wordMap.entries()].sort((a,b) => b[1] !== a[1] ? b[1] - a[1] : a[0].localeCompare(b[0]));
    console.log(sortedValue)
    return sortedValue.slice(0,k).map(x => x[0]);
};
