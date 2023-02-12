// Longest Repeating Character Replacement
// :author: SJ
// :date: Jan 27 2023
//
// You are given a string s and an integer k.
// You can choose any character of the string and change it 
//      to any other uppercase English character.
// You can perform this operation at most k times.
//
// Return the length of the longest substring 
//      containing the same letter you can get 
//      after performing the above operations.
//
//
// Example 1:
// Input: s = "ABAB", k = 2
// Output : 4
// Explanation : Replace the two 'A's with two 'B's or vice versa.
// 
// Example 2 :
// Input : s = "AABABBA", k = 1
// Output : 4
// Explanation : 
//      Replace the one 'A' in the middle with 'B' and form "AABBBBA".
//      The substring "BBBB" has the longest repeating letters, which is 4.
//




#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;


int characterReplacement(string s, int k) {
    int n = s.size();
    int i = 0, j = 0, maxi = 0;

    unordered_map<char, int> mp;

    int ans = -1;
    while (j < n)
    {
        mp[s[j]]++;
        maxi = max(maxi, mp[s[j]]);
        if ((j - i + 1) - maxi > k) {
            mp[s[i]]--;
            i++;
        }
        ans = max(ans, (j - i + 1));
        j++;
    }

    return ans;
}


int main()
{
    string str = "ABAB";
    int k = 2;

    //string str = "AABABBA";
    //int k = 1;

    int ans = characterReplacement(str, k);

    cout << ans << endl;

    return 0;
}