class Solution {
public:
    string minWindow(string s, string t) {
        unordered_map<char, int> mp;
        for(auto &ch : t) mp[ch]++;
        int count = mp.size();
        int i = 0, j = 0, n = s.size(), mini = 1e9;
        string ans = "", temp = "";
        while(i <= j && j < n){
            if(mp.find(s[j]) != mp.end()){
                mp[s[j]]--;
                if(mp[s[j]] == 0) count--;
            }
            if(count == 0){
                while(i <= j && count != 1){
                    if(mp.find(s[i]) != mp.end()){
                        mp[s[i]]++;
                        if(mp[s[i]] > 0){ 
                            count++;
                            if(mini > j-i+1){
                                mini = j-i+1;
                                ans = s.substr(i, j-i+1);
                            }
                        }
                    }
                    i++;
                }
            }
            j++;
        }
        return ans;
    }
};