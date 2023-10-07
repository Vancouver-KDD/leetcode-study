/**
 * @param {number[][]} firstList
 * @param {number[][]} secondList
 * @return {number[][]}
 */
var intervalIntersection = function (firstList, secondList) {

    if (firstList.length == 0 || secondList.length == 0) {
        return [];
    }

    //Could use Math.min || Math.max but not too sure 
    //how it will behave when the length of the lists are the same
    let firstLength = firstList.length;
    let secondLength = secondList.length;
    let firstListIndex = 0;
    let secondListIndex = 0;
    let res = [];

    while (firstListIndex < firstLength && secondListIndex < secondLength) {
        let firstElement;
        let secondElement;
        let arr = [];
        let first = firstList[firstListIndex];
        let second = secondList[secondListIndex];

        if ((first[0] >= second[0] && first[0] <= second[1]) || (first[0] <= second[0] && second[0] <= first[1])) {
            if (first[0] >= second[0] && first[0] <= second[1]) {
                firstElement = first[0];
                secondElement = Math.min(first[1], second[1]);

            } else if (first[0] <= second[0] && second[0] <= first[1]) {
                firstElement = second[0];
                secondElement = Math.min(first[1], second[1]);
            }

            arr[0] = firstElement;
            arr[1] = secondElement;
            res.push(arr);
        }

        if (first[1] > second[1]) {
            secondListIndex++;
        } else if (first[1] < second[1]) {
            firstListIndex++;
        } else {
            secondListIndex++;
            firstListIndex++;
        }
    }

    return res;

};