class Solution {
public:
    
    std::vector<int> topKFrequent(const std::vector<int>& nums, int k) {
    std::map<int, int> num_freq;
    for (int num : nums) {
        num_freq[num]++;
    }

    std::map<int, std::vector<int>> freq_to_nums;
    for (const auto& [num, freq] : num_freq) {
        freq_to_nums[freq].push_back(num);
    }

    std::vector<int> answer;
    for (auto it = freq_to_nums.rbegin(); it != freq_to_nums.rend() && (int)answer.size() < k; ++it) {
        for (int val : it->second) {
            answer.push_back(val);
            if ((int)answer.size() == k) break;
        }
    }

    return answer;
}
};