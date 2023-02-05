/**
 * You are given an integer array height of length n.
 * There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
 * Find two lines that together with the x-axis form a container, such that the container contains the most water.
 * Return the maximum amount of water a container can store.
 * Notice that you may not slant the container.
 */

// 가장 많은 용량을 담을 수 있는 두 포인터 (x-axis) 거리 * 그 두 포인터의 값중 작은 값을 tracking (to make sure the area is maximized)
// 가장 큰값을 업뎃/리턴 하는 문제

// 1. using two pointers to traverse the heights
// max var will store the maximum area found so far and be returned
// time complexity is O(N)? traverse the height array?
// I do not think it is as we only have to traverse the half of the array ..?

// Note that two pointer approach does not always has O(nlogn) time complexity 
// in this algorithm, even though we are discarding half of the remaining lines in each iteration,
// we are still performing a constant number of operations (increment/decrement & calculating max & updating max...etc)
class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        int start = 0;
        int end = height.length - 1;
        // loop continues til the start pointer >= end pointer
        while(start < end) {
            // max is updating with the max amount (multiplying the distance (right - left)
            // by minimum height of the two lines(Math.min(height[start], height[end]))
            max = Math.max(max, Math.min(height[start], height[end]) * (end - start));
            if (height[start] < height[end]) {
                start++;
            } else {
                end--;    
            } 
        }
        return max;
        
    }
}