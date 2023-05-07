/*
    Method 2: Create a Map object with value and index, and sort by desaencding value order,
                Iterate the Map object and find highest possible value filtered by index
                save the profit in the array each iteration and return highest profit in the array
*/

var maxProfit = function (prices) {
  if (prices.length === 1) {
    return 0;
  }
  if (prices.length <= 1 || prices.length >= 10 ** 5) {
    return false;
  }
  let mprices = new Map();
  for (let i = 0; i < prices.length; i++) {
    if (prices[i] < 0 || prices[i] >= 10 ** 4) return 0;
    mprices.set(i, prices[i]);
  }

  const sortedEntries = new Map(
    Array.from(mprices).sort((a, b) => a[1] - b[1])
  );

  let profit = [];
  for (let [key, value] of sortedEntries.entries()) {
    const filteredMap = new Map(
      [...sortedEntries].filter(([i, price]) => i > key)
    );
    if (filteredMap) {
      const highest = Math.max(...filteredMap.values());
      if (highest - value > 0) {
        profit.push(highest - value);
      }
    }
  }
  if (profit.length !== 0) {
    return Math.max(...profit);
  } else return 0;
};

/*
    Method 1: Find lowest value and index. filtered out where index is higher than lowest value's index
    return highest - lowest
*/

/*
    let mprices = new Map();
    for(let i=0; i< prices.length; i++){
        mprices.set(prices[i],i);
    }
    const lowest = Math.min(...mprices.keys());
    const lowest_index = mprices.get(lowest)
    if(lowest_index === prices.length -1)
        return 0
    const filteredMap = new Map([...mprices].filter(([value, i])=> i>lowest_index))
    const highest = Math.max(...filteredMap.keys());
    return highest - lowest
*/
