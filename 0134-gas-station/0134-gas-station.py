class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        summ = [0]* len(gas)
        start = 0
        tank = 0

        for i in range(len(gas)):
            summ[i] = gas[i] - cost[i]
        if sum(summ) <0:
            return -1

        for i in range(len(summ)):
            tank += summ[i] 
            if tank < 0:
                start = i + 1
                tank = 0
        return start

       