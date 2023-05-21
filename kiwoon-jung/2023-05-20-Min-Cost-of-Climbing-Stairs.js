var minCostClimbingStairs = function (cost) {
  costOfThisStep = [cost[0], cost[1]];
  for (let step = 2; step < cost.length; step++) {
    costOfThisStep[step] =
      cost[step] + Math.min(costOfThisStep[step - 1], costOfThisStep[step - 2]);
  }
  return Math.min(
    costOfThisStep[cost.length - 1],
    costOfThisStep[cost.length - 2]
  );
};
