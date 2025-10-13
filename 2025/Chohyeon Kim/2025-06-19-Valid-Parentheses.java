class Solution {
    public boolean isValid(String s) {

        Map<Character, Character> map = new HashMap<>();
        map.put('}', '{');
        map.put(')', '(');
        map.put(']', '[');

        Deque<Character> stack = new ArrayDeque<>();

        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);

            if (!map.containsKey(c)) {
                stack.push(c);
            } else {
                if (stack.isEmpty()) {
                    return false;
                }

                char left = stack.pop();

                if (map.get(c) != left) {
                    return false;
                }
            }
        }
        return stack.isEmpty();
    }
}