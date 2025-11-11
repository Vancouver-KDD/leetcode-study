/**
 * @param {number[]} temperatures
 * @return {number[]}
 */
var dailyTemperatures = function (temperatures) {
  // given a integers temperatures
  // return answers an array, answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature
  // i:2
  // v:74
  //
  // arr : 74,75,71,69,72,76,73

  const stack = [];
  const result = new Array(temperatures.length).fill(0);

  for (let i = 0; i < temperatures.length; i++) {
    while (
      stack.length > 0 &&
      temperatures[i] > temperatures[stack[stack.length - 1]]
    ) {
      const idx = stack.pop();
      result[idx] = i - idx;
    }
    stack.push(i);
  }

  return result;
};
