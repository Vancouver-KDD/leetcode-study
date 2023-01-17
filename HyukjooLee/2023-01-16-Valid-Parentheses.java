/**
 * Given a string s containing just the characters '(', ')', '{', '}', '[' and ']',  * determine if the input string is valid.
 * An input string is valid if:
 * Open brackets must be closed by the same type of brackets.
 * Open brackets must be closed in the correct order.
 * Every close bracket has a corresponding open bracket of the same type. 
*/

// 열린 괄호가 순서대로 닫히는지 그리고 닫히는 괄호와 열리는 괄호가 같은 타입인지 체크하고
// 그렇다면 true, 그렇지 않으면 false 를 리턴하는 문제입니다

// [ {,(,[,],),} ]
// 문자열이 주어진다면 문자열을 character array 로 만들고 
// loop 을 돌려서 배열의 첫번째 요소와 마지막 요소를 각각 순서대로 비교할 수 있는 data structure 를 생각해 봤을 때
// LIFO - 마지막에 들어온 요소가 첫번째로 나가는 stack 활용

// { ( [ 같이 먼저 열리는 괄호를 stack 에 푸쉬를 하고
// 다음 character 가 같은 유형의 닫히는 괄호가 나오면 pop
// 맨 마지막에 들어온 열린 괄호를 없애고 ... 반복하게 되면 stack 에 들어온 열린 괄호들은 다 없어질 것
// 마지막 isEmpty() 를 리턴하여 결과 도출

public static boolean isValid(String s) {
    	// initialize the stack
        Stack<Character> stack = new Stack<>();
        // convert string into char array
        char[] c = s.toCharArray(); 
        // traverse each char
        for(int i = 0; i < c.length; i++) {
            // the first should be open brankets
            if(c[i] == '(' || c[i] == '[' || c[i] == '{') {
                // push the char
                stack.push(c[i]);
            // check if the closing brackets appear after the corresponing open brankets
            } else if(c[i] == ')' && !stack.isEmpty() && stack.peek() == '(' ) {
                stack.pop();
            } else if(c[i] == ']' && !stack.isEmpty() && stack.peek() == '[' ) {
                stack.pop();
            } else if(c[i] == '}' && !stack.isEmpty() &&  stack.peek() == '{' ) {
                stack.pop();
            } else {
                return false;
            }
        }
            return stack.isEmpty();
    }