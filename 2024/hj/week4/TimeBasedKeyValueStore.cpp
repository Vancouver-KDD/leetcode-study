class TimeMap {
public:
    TimeMap() {

    }

    void set(string key, string value, int timestamp) {
        um[key].push_back({value, timestamp});
    }

    string get(string key, int timestamp) {
        if (um.find(key) == um.end()) {
            return "";
        }

        const auto& values = um[key];
        int l = 0, r = values.size() - 1;

        while (l <= r) {
            int mid = l + (r - l) / 2;

            if (values[mid].second == timestamp) {
                return values[mid].first;
            }

            if (values[mid].second < timestamp) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }


        return r >= 0 ? values[r].first : "";
    }

private:
    unordered_map<string, vector<pair<string, int>>> um;
};
