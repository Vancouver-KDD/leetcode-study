var totalFruit = function (fruits) {
  let baskets = [
      [-1, 0],
      [-1, 0],
    ],
    max = 1;

  let start = 0,
    end = 0;
  while (end < fruits.length) {
    /* Try to add it to a basket. */
    if (fruits[end] === baskets[0][0]) baskets[0][1]++;
    else if (fruits[end] === baskets[1][0]) baskets[1][1]++;
    else if (baskets[0][0] === -1) {
      baskets[0][0] = fruits[end];
      baskets[0][1] = 1;
    } else if (baskets[1][0] === -1) {
      baskets[1][0] = fruits[end];
      baskets[1][1] = 1;
    } else {
      /* Roll up the left side of the window. */
      while (baskets[0][1] > 0 && baskets[1][1] > 0) {
        let ind = 0;
        if (baskets[1][0] === fruits[start]) ind = 1;
        if (baskets[ind][1] === 1) baskets[ind][0] = -1;
        baskets[ind][1]--;
        start++;
      }
      continue;
    }
    max = Math.max(max, baskets[0][1] + baskets[1][1]);
    end++;
  }

  return max;
};
