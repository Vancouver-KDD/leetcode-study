// Valid Parentheses
// :author: SJ
// :date: Feb 05 2023
//
// Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
// 
// An input string is valid if:
//
// Open brackets must be closed by the same type of brackets.
// Open brackets must be closed in the correct order.
// Every close bracket has a corresponding open bracket of the same type.
//
// Example 1:
// Input: s = "()"
// Output : true
//
// Example 2 :
// Input : s = "()[]{}"
// Output : true
//    
// Example 3 :
// Input : s = "(]"
// Output : false
//


#include <iostream>
#include <string>
#include <stack>

using namespace std;

bool isValid(string s) {
    stack<char> st;
    for (auto i : s)
    {
        if (i == '(' or i == '{' or i == '[') {
            st.push(i);
        }
        else
        {
            if (st.empty() or
                (st.top() == '(' and i != ')') or
                (st.top() == '{' and i != '}') or
                (st.top() == '[' and i != ']'))
            {
                return false;
            }

            st.pop();
        }
    }

    return st.empty();
}

int main()
{
    //string str = "()";
    //string str = "()[]{}";
    string str = "(]";

    bool ans;

    ans = isValid(str);

    cout << ans << endl;
}
