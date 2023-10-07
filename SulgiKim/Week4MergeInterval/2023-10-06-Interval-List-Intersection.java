/*
 * https://leetcode.com/problems/interval-list-intersections/
 * 
 * ## Description 
 * You are given two lists of closed intervals, firstList and secondList, where firstList[i] = [starti, endi] and secondList[j] = [startj, endj]. Each list  
 *  of intervals is pairwise disjoint and in sorted order.

    Return the intersection of these two interval lists.

    A closed interval [a, b] (with a <= b) denotes the set of real numbers x with a <= x <= b.

    The intersection of two closed intervals is a set of real numbers that are either empty or represented as a closed interval. For example, the intersection of [1, 3] and [2, 4] is [2, 3].

 */



// firstList = [[0,2],[5,10],[13,23],[24,25]], secondList = [[1,5],[8,12],[15,24],[25,26]]
// i = 0 , j = 0
// startMax = max(0, 1) = 1 , endmin = min(2, 5) = 2 => ans = [1, 2], i = 1 
// i = 1, j = 0
// startMax = 5, endMin = 5 => ans += [5,5] j = 1
// i = 1 j = 1
// startMax = 8 endMin = 10 => ans += [8, 10] i = 2
// i = 2 j = 1 
// startmax = 13 endmin = 12 => j = 2  
// i = 2 j = 2 
// startMax = 15 endmin = 23 => ans += [15, 23] i = 3 
// i = 3 j = 2 
// startmax = 24 endmin = 24 => ans += [24, 24] j = 3
// i, j = 3 
// startmax = 25 endmin = 25 => ans += [25, 25] i = 4 
// return ans = [1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]

class Solution {
    public int[][] intervalIntersection(int[][] firstList, int[][] secondList) {
        //Set the pointers for each interval list 
        int i = 0; 
        int j = 0; 

        //will store the intersection value and check if it's valid 
        int startMax = 0, endMin = 0; 

        //return array 
        List<int[]> ans = new ArrayList<>();

        //iterate through both interval lists using pointers 
        while(i < firstList.length && j < secondList.length) {
            //store bigger number comparing the starting points of both interval (to take intersection)
            startMax = Math.max(firstList[i][0], secondList[j][0]);

            //store smaller number comparing the ending points of both interval (to take intersection)
            endMin = Math.min(firstList[i][1], secondList[j][1]);
            
            //if end point of intersection is placed on the right or same number with start point => valid value for answer 
            if (endMin >= startMax) {
                ans.add(new int[]{startMax, endMin});
            }

            // move the pointer depends on whether we took the ending point of firstList or secondList 
            // the pointer for the smaller ending point will move
            // so we could check intersection between the next interval of smaller ending point and current interval with bigger ending point. 
            if (endMin == firstList[i][1]) {
                i++;
            }

            if (endMin == secondList[j][1]) {
                j++;
            }
        }
        
        //convert the array list to the array to return. 
        return ans.toArray(new int[0][]);
    }
}