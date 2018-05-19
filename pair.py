

def memoized(f):
    d = dict()
    def memoized_helper(n):
        if n in d:
            return d[n]
        res = f(n)
        d[n] = res
        return res
    return memoized_helper


def memoized_static_cache(f):
    def memoized_f(n):
        if not getattr(memoized_f, 'cache', None):
            memoized_f.cache = dict()
        if n in memoized_f.cache:
            return memoized_f.cache[n]
        res = f(n)
        memoized_f.cache[n] = res
        return res
    return memoized_f

@memoized_static_cache
def _canWinNim(n):
    if n == 0:
        return False
    if n < 3:
        return True
    return not (
    _canWinNim(n - 1) and _canWinNim(n - 2) and _canWinNim(n - 3))


class Solution(object):
    def canWinNim(self, n):
        # pattern repeats [False, True, True, True, False, True, True, True...]
        return n % 4 != 0

    def canWinNim_iterative_with_arr(self, n):
        d = [False, True, True]
        for i in range(3, n+1):
            cur_val = not (d[i-1] and d[i-2] and d[i-3])
            d.append(cur_val)
        return d[n]




    def canWinNim_recursion_space_used(self, n):
        d = {0: False, 1:True, 2:True, 3:True}
        return self._canWinNim(n, d)

    def _canWinNim(self, n, d):
        if n in d:
            return d[n]
        d[n] = not (
            self._canWinNim(n - 1, d) and self._canWinNim(n - 2, d) and self._canWinNim(n - 3, d))
        return d[n]


    def canWinNimMemoizedWrapper(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return _canWinNim(n)



    def canWinNimNotMemoized(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n == 0:
            return False

        if n < 3:
            return True

        # if one of these returns False, return True
        return not (
        self.canWinNim(n - 1) and self.canWinNim(n - 2) and self.canWinNim(n - 3))





s = Solution()


# you take first stone, 1-3 stones, can you win
assert s.canWinNim(0) == False
assert s.canWinNim(1) == True
assert s.canWinNim(2) == True
assert s.canWinNim(3) == True
assert s.canWinNim(4) == False
assert s.canWinNim(5) == True
assert s.canWinNim(1348820612) == False