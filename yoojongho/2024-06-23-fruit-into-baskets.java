/**
 * Leetcode
 * problem: 904
 * link: https://leetcode.com/problems/fruit-into-baskets/
 */

class Solution {
    public int totalFruit(int[] fruits) {
        int result = 0;
        int r = -1;
        int firstItemIdx = -1, firstItemValue = 0;
        int secondItemIdx = -1, secondItemValue = 0;
        int type;

        for (int l = 0; l < fruits.length; l++) {
            type = fruits[l];
            // When first basket is empty or fruit is same type with first basket.
            if (firstItemIdx == -1 || type == firstItemValue) {
                firstItemIdx = l;
                firstItemValue = type;
            // When second basket is empty or fruit is same type with second basket.
            } else if (secondItemIdx == -1 || type == secondItemValue) {
                secondItemIdx = l;
                secondItemValue = type;
            } else {
                // When fruit is diffrent type and first basket was added first.
                if (firstItemIdx < secondItemIdx) {
                    r = firstItemIdx;
                    firstItemIdx = l;
                    firstItemValue = type;
                // When fruit is diffrent type and second basket was added first.
                } else {
                    r = secondItemIdx;
                    secondItemValue = l;
                    firstItemValue = type;
                }
            }
            result = Math.max(result, l - r);
        }
        return result;
    }
}