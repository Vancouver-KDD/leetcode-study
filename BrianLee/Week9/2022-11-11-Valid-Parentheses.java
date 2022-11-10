class Solution {
    public boolean isValid(String s) {
        Map<Character, Character> parens = new HashMap<>();

        parens.put(')', '(');
        parens.put('}', '{');
        parens.put(']', '[');

        Stack<Character> stack = new Stack<>();

        for(char c : s.toCharArray()) {
            if(parens.containsKey(c)) {
                if(stack.isEmpty()) return false;
                else {
                    if(stack.pop() != parens.get(c)) return false;
                }
            } else {
                stack.push(c);
            }
        }
        return stack.isEmpty();
    }
}