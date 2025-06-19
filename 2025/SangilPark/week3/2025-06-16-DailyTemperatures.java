package week3;
import java.util.*;

/*
 * Week 3: Stack
 * https://leetcode.com/problems/daily-temperatures/
 */
class Solution {
    public static int[] dailyTemperatures(int[] temperatures) {
        // iterate int arr -> O(n)
        // 1. brute force -> i j=i+1 / tem[i] < tem[j] -> add answer -> O(n^2)
        // 2. monotonic stack
        // -> iterate int arr, put index into stack
        // -> if tmp[stack.peek()] < tmp[i] : pop from stack and add answer
        int[] result = new int[temperatures.length];
        Stack<Integer> stack = new Stack<>();

        for (int i = 0; i < temperatures.length; i++) {
            while (!stack.isEmpty() && temperatures[stack.peek()] < temperatures[i]) {
                int idx = stack.pop();
                result[idx] = i - idx; 
            }
            stack.push(i);
        }

        return result;
    }

    public static void main(String[] args) {
        int[] input = {73,74,75,71,69,72,76,73};
        dailyTemperatures(input);
    }
}