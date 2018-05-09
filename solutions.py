
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


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

    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        count_0, count_1, count_2 = 0, 0, 0

        for n in nums:
            if n == 0:
                count_0 += 1
            elif n == 1:
                count_1 += 1
            else:
                count_2 += 1

        for i in range(len(nums)):
            if count_0:
                nums[i] = 0
                count_0 -= 1
            elif count_1:
                nums[i] = 1
                count_1 -= 1
            else:
                nums[i] = 2
                count_2 -=1

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head or not head.next:
            return False
        tortoise = head.next
        hare = head.next.next
        while hare and hare.next:
            if tortoise == head:
                return True
            tortoise = tortoise.next
            hare = hare.next.next
        return False

    def hasCycle2(self, head):
        nodes = set()
        walker = head
        while walker:
            if walker in nodes:
                return True
            nodes.add(walker)
            walker = walker.next
        return False



s = Solution()
assert s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
assert s.minCostClimbingStairs([10, 15, 20]) == 15
a = [1, 0, 1, 2]
s.sortColors(a)
assert a == [0,1,1,2]

a = ListNode(1)
b = ListNode(2)
c = ListNode(3)
d = ListNode(4)

a.next = b
b.next = c
c.next = d
d.next = a
assert s.hasCycle(a) == True

d.next = None
assert s.hasCycle(a) == False

d.next = a
assert s.hasCycle2(a) == True

d.next = None
assert s.hasCycle2(a) == False
