var maxArea = function (height) {
    // Maximum area will be stored in this variable
    let maximumArea = Number.MIN_SAFE_INTEGER;
    // Left and right pointers
    let left = 0;
    let right = height.length - 1;
    // Loop until left and right meet
    while (left < right) {
        // Shorter pole/vertical line
        let shorterLine = Math.min(height[left], height[right]);
        // Update maximum area if required
        maximumArea = Math.max(maximumArea, shorterLine * (right - left));
        // If there is a longer vertical line present
        if (height[left] < height[right]) {
            left++;
        } else {
            right--;
        }
    }
    return maximumArea;
};
