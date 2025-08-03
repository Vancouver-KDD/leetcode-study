class GasStation {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int curGas = 0, totalGas = 0;
        int start = 0;
        for (int i = 0; i < gas.length; i++) {
            int now = gas[i] - cost[i];
            curGas += now;
            totalGas += now;
            if (curGas < 0) {
                curGas = 0;
                start = i + 1;
            }
        }

        return totalGas >= 0 ? start : -1;
    }
}