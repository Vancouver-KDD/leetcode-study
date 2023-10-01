// You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits
//! where fruits[i] is the type of fruit the ith tree produces.

// You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

//! You only have two baskets, and each basket can only hold a single type of fruit.
// There is no limit on the amount of fruit each basket can hold.
// Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
//! Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
//todo: Given the integer array fruits, return the maximum number of fruits you can pick.

//* Example 1:

// Input: fruits = [1,2,1]
// Output: 3
// Explanation: We can pick from all 3 trees.

//* Example 2:

// Input: fruits = [0,1,2,2]
// Output: 3
// Explanation: We can pick from trees [1,2,2].
// If we had started at the first tree, we would only pick from trees [0,1].

//* Example 3:

// Input: fruits = [1,2,3,2,2]
// Output: 4
// Explanation: We can pick from trees [2,3,2,2].
// If we had started at the first tree, we would only pick from trees [1,2].

/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
  // fruits.length가 2보다 작거나 같으면 fruits.length를 리턴한다.
  // new Map()을 만든다.
  // maxFruits를 0으로 초기화한다.
  // start와 end를 0으로 초기화한다.
  // while문을 만든다. end가 fruits.length보다 작을 때까지 반복한다.
  // 만약 map에 fruits[end]가 없으면 map에 fruits[end]를 1로 넣는다.
  // 만약 map에 fruits[end]가 있으면 map에 fruits[end]를 1 더한다.
  // 만약 map.size가 2보다 크면 while문을 만든다. map.size가 2보다 크면 반복한다.
  // 만약 map.get(fruits[start])가 1이면 map에서 fruits[start]를 지운다.
  // 만약 map.get(fruits[start])가 1보다 크면 map에서 fruits[start]를 1 뺀다.
  // start를 1 더한다.
  // maxFruits를 Math.max(maxFruits, end - start + 1)로 한다.
  // end를 1 더한다.
  // maxFruits를 리턴한다.
  if (fruits.length <= 2) return fruits.length;
  const map = new Map();
  let start = 0;
  let end = 0;
  let maxFruits = 0;
  while (end < fruits.length) {
    if (!map.has(fruits[end])) {
      map.set(fruits[end], 1);
    } else {
      map.set(fruits[end], map.get(fruits[end]) + 1);
    }
    while (map.size > 2) {
      if (map.get(fruits[start]) === 1) {
        map.delete(fruits[start]);
      } else {
        map.set(fruits[start], map.get(fruits[start]) - 1);
      }
      start++;
    }
    maxFruits = Math.max(maxFruits, end - start + 1); // end - start + 1은 콜렉팅 한 과일의 갯수 (시작 인덱스와 끝 인덱스를 포함하기 때문에 +1)
  }
  return maxFruits;
};

// The code iterates through the array once with two pointers (start and end), and the inner while loop, which adjusts the window to contain at most two types of fruits, also runs in linear time. Therefore, the overall time complexity is dominated by the single pass through the fruits array.

// Space Complexity: O(1) since the hashmap contains at most two types of fruits.
