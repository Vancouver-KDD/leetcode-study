/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function (points, k) {
  return points
    .sort((a, b) => getDistance(a) - getDistance(b))
    .filter((item, index) => index < k);
};

/**
 * get distance point(x,y) from origin
 * @param {[int,int]} params
 * @return int
 */
const getDistance = ([x, y]) => {
  const origin = [0, 0];

  const pointX = x - origin[0];
  const pointY = y - origin[1];

  return pointX * pointX + pointY * pointY;
};
