// You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

// Find two lines that together with the x-axis form a container, such that the container contains the most water.

// Return the maximum amount of water a container can store.

const maxArea = function (height) {
  // height[i]의 값(yCoordinate)과 같거나 크면서 j-i 값이 가장 큰 height[j]를 찾아 (j - i) * height[i] 를 results에 넣고 Math.max(results) 리턴 --> O(n^2)

  // O(n)
  let result = 0;
  let l = 0;
  let r = height.length - 1;
  while (l < r) {
    let area = (r - l) * Math.min(height[l], height[r]);
    result = Math.max(result, area);

    if (height[l] < height[r]) {
      l++;
    } else r--;
  }
  return result;
};
