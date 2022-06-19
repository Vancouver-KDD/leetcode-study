function maxArea (height) {
  let area = 0;
  let left = 0;
  let right = height.length - 1;

  while(left < right) {
    const temp = (right - left) * Math.min(height[left], height[right]);
    area = Math.max(temp, area);

    if(height[left] > height[right]) {
      right -= 1;
    }else {
      left += 1;
    }
  }
  return area;
}