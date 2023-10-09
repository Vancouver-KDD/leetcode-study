// You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list of intervals is pairwise disjoint and in sorted order.

//todo: Return the intersection of these two interval lists.

// A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

// The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

//* Example 1:

// Input: firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
// Output: [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]

//* Example 2:

// Input: firstList = [[1,3],[5,9]], secondList = []
// Output: []

/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function (firstList, secondList) {
  const result = [];
  let i = 0;
  let j = 0;

  while (i < firstList.length && j < secondList.length) {
    const [start1, end1] = firstList[i];
    const [start2, end2] = secondList[j];

    // Find the intersection of two intervals
    const intersectionStart = Math.max(start1, start2);
    const intersectionEnd = Math.min(end1, end2);

    // Check if there is a valid intersection
    if (intersectionStart <= intersectionEnd) {
      result.push([intersectionStart, intersectionEnd]);
    }

    // Move the pointer of the interval that ends earlier
    if (end1 < end2) {
      i++;
    } else {
      j++;
    }
  }

  return result;
};
