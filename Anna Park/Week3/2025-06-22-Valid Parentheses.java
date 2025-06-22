import java.util.*;

class Solution {
    public boolean isValid(String s) {
        
        Stack<Character> stack = new Stack<>();
        Map<Character, Character> brackets = new HashMap<>();

        brackets.put(']', '[');
        brackets.put('}', '{');
        brackets.put(')', '(');
        
        for (char c : s.toCharArray()){
            if (stack.isEmpty()){
                stack.push(c);
            } else{
                if (stack.peek() == brackets.get(c)){
                    stack.pop();
                }
            }
        }

        if (stack.isEmpty()){
            return true;
        } else{
            return false;
        }
    }
}