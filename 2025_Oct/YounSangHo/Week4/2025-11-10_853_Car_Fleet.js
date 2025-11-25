/**
 * @param {number} target
 * @param {number[]} position
 * @param {number[]} speed
 * @return {number}
 */
var carFleet = function (target, position, speed) {
  const cars = position.map((p, i) => [p, speed[i]]);
  cars.sort((a, b) => b[0] - a[0]);

  const stack = [];

  for (const [p, s] of cars) {
    const time = (target - p) / s;
    if (!stack.length || time > stack[stack.length - 1]) {
      stack.push(time);
    }
  }

  return stack.length;
};
