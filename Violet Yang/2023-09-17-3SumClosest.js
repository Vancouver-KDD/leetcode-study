var threeSumClosest = function (nums, target) {
    // Store the total of the first 3 characters to be looked at (as we need a point of comparison)
    let closestToTarget = nums[0] + nums[1] + nums[nums.length - 1];

    // Sort the array
    const sortedNums = nums.sort((a, b) => a - b);

    // Loop through the array (excluding the last 2 entries)
    for (let i = 0; i < sortedNums.length - 2; i++) {
        // Establish a window from the next number to the end of the array
        let left = i + 1;
        let right = sortedNums.length - 1;

        // Run until the window is closed
        while (left < right) {
            // Add together the current number, and each side of the window
            const subTotal =
                sortedNums[left] + sortedNums[right] + sortedNums[i];

            // If we've found the answer
            if (subTotal == target) {
                return subTotal;
            }
            // If we're too low
            else if (subTotal < target) {
                left++;
            }
            // If we're too high
            else {
                right--;
            }

            // Check if this total is closer than the previous one
            if (
                Math.abs(subTotal - target) < Math.abs(closestToTarget - target)
            ) {
                // Store this total
                closestToTarget = subTotal;
            }
        }
    }
    return closestToTarget;
};