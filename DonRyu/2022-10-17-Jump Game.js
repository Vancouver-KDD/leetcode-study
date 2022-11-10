
var canJump = function(nums) {
  var len = nums.length;
  var max = 0;
  for (var i = 0; i < len; i++) {
    if (i > max) return false;
    max = Math.max(max, i + nums[i]);
  }
  return true;
};
