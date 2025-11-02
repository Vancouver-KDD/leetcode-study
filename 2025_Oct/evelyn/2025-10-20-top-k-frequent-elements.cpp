class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        vector<int> answer;
        int n = nums.size();

        if (n==1) return {nums[0]};

        sort(nums.begin(), nums.end());

        int idx = 1;
        priority_queue<pair<int, int>> idx_q;

        for (int i = 1; i < n; i++) {
            if (nums[i-1] != nums[i]) {
                idx_q.push({idx, nums[i-1]});
                idx = 1;
            } else idx++;
        }

        idx_q.push({idx, nums[n-1]});

        for (int j=0; j < k; j++) {
            auto cand = idx_q.top();
            answer.push_back(cand.second);
            idx_q.pop();
        }
        
        return answer;
    }
};

class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> freq;
        for (int num : nums) freq[num]++;

        int maxFreq = 0;
        for (auto& [num, count] : freq) {
            maxFreq = max(maxFreq, count);
        }

        vector<vector<int>> bucket(maxFreq + 1);
        for (auto& [num, count] : freq) {
            bucket[count].push_back(num);
        }

        vector<int> result;
        for (int i = maxFreq; i >= 1 && result.size() < k; --i) {
            for (int num : bucket[i]) {
                result.push_back(num);
                if (result.size() == k) break;
            }
        }

        return result;
    }
};