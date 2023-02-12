// Input: prices = [7,1,5,3,6,4]
// Output: 5
// Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
// Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

/**
 * https://leetcode.com/problems/minimum-window-substring/
 * Time O(N + M) | SpaceO(N + M)
 * @param {string} s
 * @param {string} t
 * @return {string}
 */
 var minWindow = function (s, t) {
    const isMissingArgs = !s.length || !t.length;
    if (isMissingArgs) return '';

    const frequencyMap = getFrequencyMap(t);
    const { start, end } = getWindowPointers(s, t, frequencyMap);

    return getSubString(s, start, end);
};

const getFrequencyMap = (str, frequencyMap = new Map()) => {
    for (const char of str) {
        frequencyMap.set(char, (frequencyMap.get(char) || 0) + 1);
    }

    return frequencyMap;
};

const getWindowPointers = (s, t, frequencyMap) => {
    let [left, right, matched, start, end] = [0, 0, 0, 0, s.length + 1];

    while (right < s.length) {
        matched = addRightFrequency(s, right, frequencyMap, matched);

        const canSlide = () => matched === t.length;
        while (canSlide()) {
            const window = right - left + 1;

            const isSmaller = window < end;
            if (isSmaller) {
                [start, end] = [left, window];
            }

            matched = subtractLeftFrequency(s, left, frequencyMap, matched);
            left++;
        }

        right++;
    }

    return { start, end };
};

const addRightFrequency = (s, right, frequencyMap, matched) => {
    const char = s[right];

    if (frequencyMap.has(char)) {
        frequencyMap.set(char, frequencyMap.get(char) - 1);

        const isInWindow = 0 <= frequencyMap.get(char);
        if (isInWindow) matched++;
    }

    return matched;
};

const subtractLeftFrequency = (s, left, frequencyMap, matched) => {
    const char = s[left];

    if (frequencyMap.has(char)) {
        const isOutOfWindow = frequencyMap.get(char) === 0;
        if (isOutOfWindow) matched--;

        frequencyMap.set(char, frequencyMap.get(char) + 1);
    }

    return matched;
};

const getSubString = (s, start, end) =>
    end <= s.length ? s.slice(start, start + end) : '';