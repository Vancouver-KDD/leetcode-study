class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> um;
        priority_queue<pair<int, int>> pq;
        vector<int> output;

        for (auto &num : nums) {
            um[num]++;
        }

        for (auto &pair : um) {
            pq.push({pair.second, pair.first});
        }

        while (k > 0) {
            output.push_back(pq.top().second);
            pq.pop();
            k--;
        }

        return output;
    }
};
