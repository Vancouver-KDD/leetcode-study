
//limitation:  s is null -> return 0
//Input: s = "()" -->  Output: true
//Input: s = "()[]{}" --> Output: true
//Input: s = "(]" -->  Output: false
//Input: s = "(({[" -->  Output: false

//2023-01-28
//Time Complexity: 
//Space Complexity: 
class Solution{
    public boolean isValid(String s){
        if(s == null || s.length() == 0){
            return false;
        }

        HashMap<Character, Character> map = new HashMap<>();
        map.put(')','(');
        map.put('}','{');
        map.put(']','[');
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                if(!stack.isEmpty()){
                    char bracket = stack.pop();
                    if(bracket != map.get(ch)){
                        return false;
                    }
                }else{
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }

        return stack.isEmpty();
    }
}

//2022-12-05
//Time Complexity: O(N)
//Space Complexity: O(N)
/*
class Solution{
    public boolean isValid(String s){
        if(s == null || s.length() == 0){
            return false;
        }

        HashMap<Character, Character> bracketMap = new HashMap<>();
        bracketMap.put(')','(');
        bracketMap.put('}','{');
        bracketMap.put(']','[');

        Stack<Character> stack = new Stack<>();

        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(bracketMap.containsKey(ch)){
                if(stack.isEmpty()){
                    return false;
                }
                char bracket = stack.pop();
                if(bracket != bracketMap.get(ch)){
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }

        return stack.isEmpty();
    }
}
*/
//2022-11-13
//Time complexity: O(N), Space complexity:O(N)
/*
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
*/
//Time complexity: O(N), Space complexity:O(N) 
//2022-08-21
/*
class Solution {
    
    public boolean isValid(String s){
        
        if( s == null || s.length() == 0){
            return false;
        }
        
        HashMap<Character, Character> map = new HashMap<>();
        
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
        
        Stack<Character> stack = new Stack<Character>();
        
        for(int i = 0; i < s.length(); i++){
            if(!map.containsKey(s.charAt(i))){
                stack.push(s.charAt(i));
            }else{
                if(!stack.empty()){
                    char ch = stack.pop();
                    if(ch != map.get(s.charAt(i))){
                        return false;
                    }
                }else{ // there is no matching open bracket
                    return false;
                }
            }
        }
               
        if(stack.empty()){
            return true;
        }else{
            return false;
        }
        
        
    }
}
*/
// 2022-06-10
/*
class Solution {
    
    static Map<Character, Character> map = new HashMap<>();
    static{
        map.put(')', '(');
        map.put('}', '{');
        map.put(']', '[');
    }
    
    public boolean isValid(String s){
        
        if(s == null || s.length() == 0){
            return false;
        }
        
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            
            Character ch = s.charAt(i);
            if(map.containsKey(ch)){
                if(stack.empty() || stack.pop() != map.get(ch)){
                    return false;
                }
            }else{ //push to stack
                stack.push(ch);
            }
        }
        
        if(!stack.empty()){
            return false;  // not matched brackets
        }
        
        return true;
        
    }
  
}
*/

/*
class Solution {
    
    private Map<Character, Character> map = new HashMap<>();
    
    public Solution(){
        this.map.put(')', '(');
        this.map.put('}', '{');
        this.map.put(']', '[');
    }
    
    public boolean isValid(String s){
        Stack<Character> stack = new Stack<>();
        
        for(int i = 0; i < s.length(); i++){
            char ch = s.charAt(i);
            if(map.containsKey(ch)){
                
                char topCh = stack.empty() ? '#' : stack.pop();
                
                if(topCh != map.get(ch)){
                    return false;
                }
            }else{
                stack.push(ch);
            }
        }        
        return stack.empty();
    }
  
}
*/

/*
class Solution {
    
    static String[] parentheses = new String[]{"(",")", "{", "}", "[", "]"};
    
    static Map<Character, Integer> map = new HashMap<>();
    static{
        map.put('(', 0);
        map.put(')', 1);
        map.put('{', 2); 
        map.put('}', 3);
        map.put('[', 4);
        map.put(']', 5);
    }
    
    public boolean isValid(String s) {
        
        Stack pthStack = new Stack<Character>();        
        int count = 0;
        
        while(count < s.length()){
            char ch = s.charAt(count);
            if(map.containsKey(ch)){
                
                int index = map.get(ch);
                if((index %2) == 0){
                    pthStack.push(ch);
                }else{
                    if(pthStack.empty()){
                        return false;
                    }
                    char item = (char)(pthStack.pop());
                    //System.out.println("s: "+ch+", "+index+"), item: " + item + ", "+map.get(item));
                    //int openPth = map.get(item) -1;

                    if((index-1) != map.get(item)){
                        return false;
                    }
                }
            }else{
                return false;
            }
            
            count++;
        }
        
        return pthStack.empty();
    }

}
*/
