/**
 * @param {number[]} nums
 * @param {number} goal
 * @return {number}
 */
var numSubarraysWithSum = function (nums, goal) {
  let count = 0; // 결과를 저장할 변수

  // 누적 합을 저장할 객체
  const sumCount = new Map();
  let sum = 0;

  // 초기값 설정
  sumCount.set(0, 1);

  for (const num of nums) {
    sum += num;

    // 현재까지의 누적 합 중에서 (현재 합 - goal)인 값을 가진 경우를 찾아 개수를 더합니다.
    if (sumCount.has(sum - goal)) {
      count += sumCount.get(sum - goal);
    }

    // 현재 합을 누적 합으로 저장합니다.
    sumCount.set(sum, (sumCount.get(sum) || 0) + 1);
  }

  return count;
};
