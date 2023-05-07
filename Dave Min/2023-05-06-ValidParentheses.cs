public class Solution {
    public bool IsValid(string s) {
        Dictionary<char,char> pair = new Dictionary<char,char>();
        pair.Add(')','(');
        pair.Add(']','[');
        pair.Add('}','{');

        Stack<char> stk = new Stack<char>();

        foreach(var c in s){                        
            if(stk.Count() == 0 && pair.ContainsKey(c)) return false;

            if(pair.ContainsKey(c) && stk.Peek() == pair[c]) stk.Pop();
            else stk.Push(c);
        }

        return stk.Count == 0? true:false;
    }
}


//Time complexity: O(N);
//Space complexity: O(N); WorstCase = "{{{{{{{{{{{{{......"
