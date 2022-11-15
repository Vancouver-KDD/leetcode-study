//limitation:  s is null -> return 0
//Input: s = "()" -->  Output: true
//Input: s = "()[]{}" --> Output: true
//Input: s = "(]" -->  Output: false
//Input: s = "(({[" -->  Output: false

//Time complexity: O(N), Space complexity:O(N)
//2022-11-13
class Solution{
    public boolean isValid(String s){

        if(s == null || s.length() == 0){
            return false;
        }
        HashMap<Character, Character> brackets = new HashMap<>();

        brackets.put(')', '(');
        brackets.put('}', '{');
        brackets.put(']', '[');

        Stack<Character> parentheses = new Stack<Character>();
        for(int i = 0; i < s.length(); i++){
            if(brackets.containsKey(s.charAt(i))){ // close brackets
                if(parentheses.isEmpty()){
                    return false;
                }
                char ch = parentheses.pop();
                if( ch != brackets.get(s.charAt(i))){
                    return false;
                }
            }else{//open bracket
                parentheses.push(s.charAt(i));
            }
        }

        if(parentheses.isEmpty()){
            return true;
        }

        return false;
    }
}