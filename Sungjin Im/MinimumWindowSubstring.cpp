// Minimum Window Substring
// :author: SJ
// :date: Jan 27 2023
//
// Given two strings s and t of lengths m and n respectively,
// return the minimum window substring of s
//      such that every character in t(including duplicates) is included in the window.
// 
// If there is no such substring,
//      return the empty string "".
//
// The testcases will be generated 
//      such that the answer is unique.
//
// Example 1:
// Input: s = "ADOBECODEBANC", t = "ABC"
// Output : "BANC"
// Explanation : The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
//
// Example 2 :
// Input : s = "a", t = "a"
// Output : "a"
// Explanation : The entire string s is the minimum window.
//
// Example 3 :
// Input : s = "a", t = "aa"
// Output : ""
// Explanation : Both 'a's from t must be included in the window.
// Since the largest window of s only has one 'a', return empty string.
//


#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;


string minWindow(string s, string t) {
    int m = s.size(), n = t.size();
    unordered_map<char, int> mp;

    int ans = INT_MAX;
    int start = 0;

    for (auto x : t)
        mp[x]++;

    int count = mp.size();

    int i = 0, j = 0;

    while (j < s.length()) {
        mp[s[j]]--;
        if (mp[s[j]] == 0)
            count--;

        if (count == 0) {
            while (count == 0) {
                if (ans > j - i + 1) {
                    ans = j - i + 1;
                    start = i;
                }
                mp[s[i]]++;
                if (mp[s[i]] > 0)
                    count++;

                i++;
            }
        }
        j++;
    }
    if (ans != INT_MAX)
        return s.substr(start, ans);
    else
        return "";
}

int main()
{
    string s = "ADOBECODEBANC";
    string t = "ABC";

    //string s = "a";
    //string t = "a";

    //string s = "a";
    //string t = "aa";

    string ans = minWindow(s, t);

    cout << ans << endl;

    return 0;
}