package week3;
import java.util.*;

/*
 * Week 3: Stack
 * https://leetcode.com/problems/valid-parentheses/
 */
class Solution {
    public static boolean isValid(String s) {
        // stack - open : push
        // closed -> false / only same type bracket
        Stack<Character> stack = new Stack<>();

        for (char c : s.toCharArray()) {
            if (c == ')' || c == ']' || c == '}') {     // close brackets
                if (stack.isEmpty()) return false;

                char open = stack.pop();
                if (open == '(' && c == ')'
                    || open == '[' && c == ']'
                    || open == '{' && c == '}') continue;

                return false;
            } else {                // open brackets
                stack.push(c);
            }
        }

        return stack.isEmpty();
    }

    public static void main(String[] args) {
        isValid("()[]{}");
    }
}