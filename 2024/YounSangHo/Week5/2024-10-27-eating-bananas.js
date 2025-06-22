class Solution {
  /**
   * @param {number[]} piles
   * @param {number} h
   * @return {number}
   */
  minEatingSpeed(piles, h) {
    // k이라는 값을 구해야한다
    // k는 시간당 먹는 양
    // 전체 바나나를 먹는데 h시간을 초과 해선 안된다.
    // k개는 h시간 내에 시간당 가장 적게 먹어야 한다.
    // k의 범위는 1 부터 바나나 piles[i]중 가장 큰값으로 한다.
    // [Intuition]
    // In this exam, we need to find out how many bananas we have to eat per hour between the starting pile amount of 1, to the largest pile amount.
    // The number of bananas eaten per hour should be the smallest value nor exceeding h hours.
    // [Approach]
    // We will use Binary Search
    // We imagine an array which is banana numbers 1 to most big numbers in piles

    // Method 1: Brute-force (Merging the arrays)
    // Merge the two arrays: Since both nums1 and nums2 are sorted, we can use the two-pointer technique to merge them into a new sorted array. We start from the first elements of both arrays and compare them, inserting the smaller element into the new array. We continue this until all elements from both arrays are added.

    // Find the median: Once we have a merged array, the median is straightforward to compute:

    // If the total number of elements is odd, the median is the middle element.
    // If the total number of elements is even, the median is the average of the two middle elements.
    // The brute-force approach works but has a time complexity of O(n1 + n2) due to merging the arrays, which is not optimal when dealing with large datasets.

    // Method 2: Binary Search for Optimized Median Finding
    // This method leverages binary search to find the median without merging the arrays.

    // Idea: The key observation is that we are looking for the median, which divides the merged arrays into two halves. We can perform binary search on one of the arrays to partition both arrays in such a way that the left half contains the smaller numbers, and the right half contains the larger numbers.

    // Time complexity: By applying binary search, we reduce the time complexity to O(log(min(n1, n2))), which is more efficient, especially for large arrays.

    // [Complexity Analysis]
    // Time complexity:
    // Method 1 (Brute-force): O(n1 + n2) due to merging both arrays.
    // Method 2 (Binary search): O(log(min(n1 ,n2))) as we use binary search to partition the arrays and find the median efficiently.

    // Space complexity:
    // Method 1 (Brute-force): O(n1 +n2) since we store the entire merged array.
    // Method 3 (Binary search): O(1) as we only use a few variables for partitioning.

    let right = 1;
    let left = Math.max(...piles);
    let results = 0;

    while (right <= left) {
      let mid = Math.floor((right + left) / 2);
      let totalHour = 0;

      piles.forEach((pile) => {
        totalHour += Math.ceil(pile / mid);
      });

      if (totalHour > h) {
        right = mid + 1;
      } else {
        results = mid;
        left = mid - 1;
      }
    }

    return results;
  }
}
