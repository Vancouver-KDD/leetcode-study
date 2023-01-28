// Longest Substring Without Repeating Characters
// :author: SJ
// :date: Jan 27 2023
//
// Given a string s,
//      find the length of the longest substring
//      without repeating characters.
//
// Example 1:
// Input: s = "abcabcbb"
// Output : 3
// Explanation : The answer is "abc", with the length of 3.
// 
// Example 2 :
// Input : s = "bbbbb"
// Output : 1
// Explanation : The answer is "b", with the length of 1.
//
// Example 3 :
// Input : s = "pwwkew"
// Output : 3
// Explanation : The answer is "wke", with the length of 3.
// Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
//

#include <iostream>
#include <string>
#include <unordered_set>

using namespace std;

int lengthOfLongestSubstring(string s)
{
	unordered_set<char> set;

	int i = 0, j = 0, n = s.size(), ans = 0;

	while (i < n && j < n)
	{
		if (set.find(s[j]) == set.end()) //If the character does not in the set
		{
			set.insert(s[j++]); //Insert the character in set and update the j counter
			ans = max(ans, j - i); //Check if the new distance is longer than the current answer
		}
		else
		{
			set.erase(s[i++]);
			/*If character does exist in the set, ie. it is a repeated character,
			we update the left side counter i, and continue with the checking for substring. */
		}
	}

	return ans;
}

int main()
{
	string str = "abcabcbb";
	//string str = "bbbbb";
	//string str = "pwwkew";
	
	int ans;

	ans = lengthOfLongestSubstring(str);

	cout << ans << endl;

	return 0;
}