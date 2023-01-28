/**
 * Given an integer array nums, return an array answer such that
 * answer[i] is equal to the product of all the elements of nums except nums[i].
 * The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 * You must write an algorithm that runs in O(n) time and without using the division operation.
 */


// 1. using prefix and suffix 
//     [1,  2,  3,  4,  5,  6]
//pre   1   1   2   6   24 120
//suf  720 360 120  30  6   1
//res  720 360 240  180 144 1
// prefix(left) 는 왼쪽에 있는 모든 원소의 곱을 포함
// suffix(right) 는 오른쪽에 있는 모든 원소의 곱을 포함
// result 는 왼쪽에 있는 모든 원소의 곱 * 오른쪽에 있는 모든 원소의 곱, 즉 자신을 제외한 모든 원소의 곱이 된다
// time complexity is 0(3n) =>  O(n)
// space complexity is 0(n)
class Solution {
 public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] left = new int[length];
        int[] right = new int[length];
        int[] result = new int[length];

        // 처음 인덱스 0은 왼쪽, 오른쪽에 있는 원소의 곱이 없음, 즉 value 를 1 로 초기화
        left[0] = 1;
        right[length -1] = 1;
        for(int i = 1; i < length; i++) {
            left[i] = nums[i-1] * left[i-1];
        }
        for(int i = length -2; i >= 0; i--) {
            right[i] = nums[i + 1] * right[i + 1];
        }
        // result
        for(int i = 0; i < length; i++) {
            result[i] = left[i] * right[i];
        }
        return result;
    }
}

// 2. using extra constant space - more efficient in terms of space complexity
// As output array does not count as extra space for space complexity analysis, space complexity is O(1)
class Solution {
 public int[] productExceptSelf(int[] nums) {
        int length = nums.length;
        int[] result = new int[length];

        // to take constant extra space
        // pre
        result[0] = 1;

        // from left to right
        // use prefix products temporarily
        for (int i = 1; i < length; i++) {
            result[i] = result[i-1] * nums[i-1];
        }

        int right = 1;
        for (int i = length -1; i >= 0; i--) {
            result[i] = result[i] * right;
            right *= nums[i];
        }

        return result;
    }
}