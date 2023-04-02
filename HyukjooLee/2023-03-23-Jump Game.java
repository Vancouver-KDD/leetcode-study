// You are given an integer array nums. You are initially positioned at the array's first index, 
// and each element in the array represents your maximum jump length at that position.

// Return true if you can reach the last index, or false otherwise.

// Input: nums = [2,3,1,1,4]
// Output: true
// Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

// 인덱스 0 에서 시작하고, 각 해당 인덱스에서의 values 는 최대 점프길이
// 마지막 인덱스에 도달 가능하면 true, otherwise false

// greedy approach? selects the best option available at the current moment

// for cases like {4, 1, 3, 1, 0, 5}, 
// the greedy algorithm can jump from index 0 by 4 to reach the 4th index
// but after that, it can't reach the last index because it only has to jump by 1 or 0?

// maxReach = Math.max(farthest, i + nums[i]); 'at the each current moment'
// means that we iterate (i = 0; i < n; i++)

// time complexity is O(N): the length of the array
// space complexity is O(1): constant vars
public static boolean canJump(int[] nums) {
    int farthest = 0;
    int n = nums.length;

    for (int i = 0; i < n; i++) {
        if (i > farthest) {
            return false;
        }
        farthest = Math.max(farthest, i + nums[i]);
        if (farthest >= n - 1) {
            return true;
        }
    }

    return false;
}
