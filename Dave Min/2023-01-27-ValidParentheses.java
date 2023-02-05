import java.util.*;
import java.io.*;

class Solution {
    public boolean isValid(String s) {
        Stack<Character> stc = new Stack<Character>();

        for(int i=0;i<s.length();i++){
            if(s.charAt(i) == ']'){
                if(stc.size() != 0 && stc.pop() == '[')  continue;
                else return false;
            }
            if(s.charAt(i) == '}'){
                if(stc.size() != 0 && stc.pop() == '{')  continue;
                else return false;
            }
            if(s.charAt(i) == ')'){
                if(stc.size() != 0 && stc.pop() == '(')  continue;
                else return false;
            }  
            stc.push(s.charAt(i));
        }

        if(stc.size() != 0){
            return false;
        }
        return true;

    }
}