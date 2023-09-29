/* https://leetcode.com/problems/fruit-into-baskets/
 * 
 * ## Description 
 * You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where
 *  fruits[i] is the type of fruit the ith tree produces.

    You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

    You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
    Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
    Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
    Given the integer array fruits, return the maximum number of fruits you can pick.
 * 
 * 
 */

 class Solution {
    public int totalFruit(int[] fruits) {
        int type1 = -1, type2 = -1; //1: second last fruit type, 2: last fruit type
        int lastFruitCount = 0; //count of type 2
        int currentMax = 0, max = 0; 

        for (int fruit : fruits) {
            if (fruit == type1 || fruit == type2) {
                currentMax++; 
            } else {
                currentMax = lastFruitCount + 1; 
            }

            if (fruit == type2) {
                lastFruitCount++;
            } else {
                lastFruitCount = 1; 
                type1 = type2; 
                type2 = fruit;
            }

            max = Math.max(currentMax, max);
        }
        return max;
    }
}