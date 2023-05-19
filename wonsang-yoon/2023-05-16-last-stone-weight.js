/**
 * @param {number[]} stones
 * @return {number}
 */
var lastStoneWeight = function (stones) {
    if(stones.length === 1){return stones[0]}
    while (stones.length >= 1) {
        let stone1 = Math.max(...stones);
        stones.splice(stones.indexOf(stone1), 1);
        let stone2 = Math.max(...stones);
        stones.splice(stones.indexOf(stone2), 1);
        let diff = Math.abs(stone1 - stone2);
        stones.push(diff);

        if (stones.length === 1) {
            return stones[0]
        }
    }
    return 0

};