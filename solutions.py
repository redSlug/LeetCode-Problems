

class Solution:
    def minCostClimbingStairs(self, cost):
        if len(cost) == 1:
            return 0
        cache = [None] * len(cost)
        i = -1
        return self._min_cost_helper(cost, i, cache)

    def _min_cost_helper(self, cost, i, cache):
        if i+2 >= len(cost):
            return cost[i]

        if cache[i]:
            return cache[i]

        c = self._min_cost_helper(cost, i + 1, cache) + (cost[i] if len(cost) > i >= 0 else 0)
        d = self._min_cost_helper(cost, i + 2, cache) + (cost[i] if len(cost) > i >= 0 else 0)
        min_cost = min(c, d)
        cache[i] = min_cost
        return min_cost


s = Solution()
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert s.minCostClimbingStairs([10, 15, 20]) == 15
