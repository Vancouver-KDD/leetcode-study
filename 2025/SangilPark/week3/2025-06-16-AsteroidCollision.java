package week3;
import java.util.*;

/*
 * Week 3: Stack
 * https://leetcode.com/problems/asteroid-collision/
 */
class Solution {
    public static int[] asteroidCollision(int[] asteroids) {
        // stack : positive value
        // iterate over array -> case (+) (-) : evaulate size
        Stack<Integer> stack = new Stack<>();

        for (int asteroid : asteroids) {
            boolean isCollised = false;

            while (!stack.isEmpty() && stack.peek() > 0 && asteroid < 0) {
                int top = stack.peek();

                if (top > -asteroid) {
                    isCollised = true;
                    break;
                } else if (top < -asteroid) {
                    stack.pop();
                } else {
                    stack.pop();
                    isCollised = true;
                    break;
                }
            }

            if (!isCollised) {
                stack.push(asteroid);
            }
        }

        int size = stack.size();
        int[] result = new int[size];
        for (int i = size - 1; i >= 0; i--) {
            result[i] = stack.pop();
        }
        return result;
    }

    public static void main(String[] args) {
        int[] input = {-2,-2,1,-2};
        asteroidCollision(input);
    }
}