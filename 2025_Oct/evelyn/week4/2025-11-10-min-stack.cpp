#include <vector>
#include <algorithm>
#include <stdexcept>

class MinStack {
private:
    std::vector<int> s;
    std::vector<int> min_s;

public:
    MinStack() {}

    void push(int val) {
        s.push_back(val);
        if (min_s.empty() || val <= min_s.back()) {
            min_s.push_back(val);
        }
    }

    void pop() {
        if (s.empty()) return;
        if (s.back() == min_s.back()) {
            min_s.pop_back();
        }
        s.pop_back();
    }

    int top() {
        if (s.empty()) throw std::runtime_error("Stack is empty");
        return s.back();
    }

    int getMin() {
        if (min_s.empty()) throw std::runtime_error("Stack is empty");
        return min_s.back();
    }
};
