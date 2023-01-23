// Group Anagrams
// :author: SJ
// :date: Jan 18-21 2023
//
// Given an array of strings strs,
// group the anagrams together.
// You can return the answer in any order.
//
// Example 1:
// Input: strs = ["eat","tea","tan","ate","nat","bat"]
// Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
//
// Example 2:
// Input: strs = [""]
// Output : [[""]]
//
// Example 3 :
// Input : strs = ["a"]
// Output : [["a"]]
//

#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <utility>

using namespace std;


#define _RUN_MODE

int main()
{
	vector<string> strs = { "eat","tea","tan","ate","nat","bat" };
//	vector<string> strs = { "" };
//	vector<string> strs = { "a" };

	vector<pair<string, int>> paired_strs;


	for (int i = 0; i < strs.size(); i++) {
		paired_strs.push_back(make_pair(strs[i], i));
	}

#ifndef _RUN_MODE		// means if debug mode
	for (int i = 0; i < paired_strs.size(); i++) {
		cout << paired_strs[i].first << "\t" << paired_strs[i].second << "\n";
	}
	cout << "\n\n";
#endif
	
	
	for (int i = 0; i < paired_strs.size(); i++) {
		sort(paired_strs[i].first.begin(), paired_strs[i].first.end());
	}


	sort(paired_strs.begin(), paired_strs.end());

	
#ifndef _RUN_MODE		// means if debug mode
	for (int i = 0; i < paired_strs.size(); i++) {
		cout << paired_strs[i].first << "\t" << paired_strs[i].second << "\n";
	}
	cout << "\n\n";
#endif



	cout << "[[\"";
	string cur_str = "";

	for (int i = 0; i < paired_strs.size(); i++) {
			if (cur_str == "") {
				cout << strs[paired_strs[i].second];
				cur_str = paired_strs[i].first;
			}
			else {
				if (cur_str.compare(paired_strs[i].first) == 0) {
					cout << "\",\"";
					cout << strs[paired_strs[i].second];
					cur_str = paired_strs[i].first;
				}
				else {
					cout << "\"],[\"";
					cout << strs[paired_strs[i].second];
					cur_str = paired_strs[i].first;
				}

			}
	}


	cout << "\"]]";

	cout << "\n\n";

	
	return 0;
}
