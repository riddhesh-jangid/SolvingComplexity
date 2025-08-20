from functools import lru_cache

class Solution:
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def make_recursion(decode, n):
            
            if decode=='':
                pass
            elif decode[0]=='0':
                return 0
            elif int(decode)>26:
                return 0

            if n == -1 or n == -2:
                return 1

            two=0
            one=0

            if n>0:            
                two = make_recursion(nums[n-1]+nums[n], n-2)

            if n>-1:
                one = make_recursion(nums[n], n-1)

            return two + one

        nums = [c for c in s]
        print(nums)
        return make_recursion('', len(nums)-1)