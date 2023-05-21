var lastStoneWeight = function (stones) {
  if (stones.length == 1) {
    // base case
    return stones;
  } else if (stones.length == 0) {
    // base case
    return 0;
  }
  let heavy1 = Math.max(...stones); // grabs heaviest stone
  stones.splice(stones.indexOf(heavy1), 1); // removes heaviest stone
  let heavy2 = Math.max(...stones); // grabs 2nd heaviest stone
  stones.splice(stones.indexOf(heavy2), 1); // removes 2nd heaviest stone
  if (heavy1 > heavy2) {
    let newStone = heavy1 - heavy2; // find difference
    stones.push(newStone); // push difference to stones
  }
  // calls on the function again until base case is true
  return lastStoneWeight(stones);
};
