/**
 * @param {number[]} fruits
 * @return {number}
 */
var totalFruit = function (fruits) {
    let n = fruits.length;
    if (n <= 2) {
        return n;
    }

    let max = 0;
    // end is the end of the array
    // first and second basket is the number of fruits in the basket currently
    // treeOne and treeTwo are # of trees fruits are picked from
    let end = 0,
        firstBasket = 0,
        secondBasket = 0,
        treeOne = null,
        treeTwo = null;

    while (end < n) {

        // if the fruit is from a new tree, second tree / basket becomes first tree / basket
        if (treeTwo == null) {
            treeTwo = fruits[end];
            secondBasket = 1;
        } else if (fruits[end] != treeOne && fruits[end] != treeTwo) {
            treeOne = fruits[end - 1];
            firstBasket = 0;
            for (let i = end - 1; i >= 0; i--) {
                if (fruits[i] != treeOne) {
                    break;
                }
                firstBasket++;
            }
            treeTwo = fruits[end];
            secondBasket = 1;
        } else if (fruits[end] == treeOne) {
            firstBasket++;
        } else {
            secondBasket++;
        }
        end++;
        let curr = firstBasket + secondBasket;
        max = Math.max(max, curr);
    }

    return max;
};