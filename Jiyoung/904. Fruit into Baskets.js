var totalFruit = function (fruits) {
    let prevType = -1;
    let lastType = -1;

    let lastTypeCount = 0;

    let currentMax = 0;
    let max = 0;

    for (const fruit of fruits) {
        if (fruit === prevType || fruit === lastType) {
            currentMax++;
        } else {
            currentMax = lastTypeCount + 1;
        }

        if (fruit === lastType) {
            lastTypeCount++;
        } else {
            prevType = lastType;
            lastType = fruit;
            lastTypeCount = 1;
        }

        max = Math.max(currentMax, max);
    }

    return max;
};
