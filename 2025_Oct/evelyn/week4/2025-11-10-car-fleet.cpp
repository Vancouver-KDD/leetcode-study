class Solution {
public:
    int carFleet(int target, vector<int>& position, vector<int>& speed) {

        vector<pair<int, double>> cars;

        for (int i = 0; i < position.size(); i++) {
            double time = (double)(target - position[i]) / speed[i];
            cars.push_back({position[i], time});
        }

        sort(cars.begin(), cars.end(), [](auto &a, auto &b){
            return a.first > b.first;
        });

        int fleets = 0;
        double slowTime = 0;

        for (auto &c : cars) {
            if (c.second > slowTime) {
                fleets++;
                slowTime = c.second;
            }
        }

        return fleets;
    }
};
