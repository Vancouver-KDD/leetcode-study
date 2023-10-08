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

//////////////
function calc(arr) {
  let q = new Set();
  let result = 0;
  let total = 0; //해당 total의 set에 설정되어 있는 각 objects의 total 합의 되어야함
  let left = 0;

  for (let j = 0; j < arr.length; j++) {
    // make the hash table with the given array
    if (q.has(arr[j])) {
      q.set(arr[j], q.get(arr[j]) + 1);
      total++;
    } else {
      q.set(arr[j], 1);
      total++;
    }

    while (q.size > 2) {
      q.delete(arr[left]);
      q.set(arr[left], q.get(arr[left] - 1));
      total--;
      left++;
    }

    result = Math.max(result, total);
  }

  return result;
}
