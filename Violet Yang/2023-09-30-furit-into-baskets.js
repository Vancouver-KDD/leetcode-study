var totalFruit = function(fruits) {
    const newSorted = fruits.reduce((result, fruit)=> {
        result[fruit] = (result[fruit] || 0) + 1
        return result
    },{})
    const fruitCnt = Object.values(newSorted).sort((a,b)=> b-a).filter((el, idx)=> idx <= 1)
    console.log(fruitCnt)
    const sumCnt = fruitCnt.reduce((sum ,cnt)=> (sum += cnt),0)
    return sumCnt

};
