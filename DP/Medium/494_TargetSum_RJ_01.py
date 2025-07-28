from functools import lru_cache

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        @lru_cache(None)
        def make_recursion(calculated, e):

            if e<0:
                if calculated==target:
                    return 1
                else:
                    return 0

            s1 = make_recursion(calculated+nums[e], e-1)
            s2 = make_recursion(calculated-nums[e], e-1)

            return s1+s2
         
        return make_recursion(0, len(nums)-1)
        