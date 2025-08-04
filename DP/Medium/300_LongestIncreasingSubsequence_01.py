class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        cache = {}
        def make_recursion(last, i):
            
            if i == len(nums):
                return 0
            
            if (last,i) in cache.keys():
                return cache[(last,i)]
            
            # skip
            skip = make_recursion(last, i+1)

            if last >= nums[i]:
                return skip

            # include
            include = 1 + make_recursion(nums[i] ,i+1)

            result = max(skip, include)
            cache[(last,i)] = result
            return result


        return make_recursion(-10000,0)