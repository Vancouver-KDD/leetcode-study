class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {
        map<int,int> meetings;
        for (auto& interval : intervals) {
            meetings[interval[0]]++;
            meetings[interval[1]]--;
        }
        
        int rooms = 0, maxRooms = 0;
        for (auto& [k,v] : meetings) {
            rooms += v;
            maxRooms = max(maxRooms, rooms);
        }
        
        return maxRooms;
    }
};
