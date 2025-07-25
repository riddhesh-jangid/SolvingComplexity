from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        EQUAL = sum(nums)/2
        cache = {}
        def skipOrInclude(SUM, i):
            
            # base condition
            if SUM > EQUAL or i<0:
                return False
            
            if SUM == EQUAL:
                return True

            if (SUM,i) in cache:
                return cache[(SUM,i)]

            state = skipOrInclude(SUM, i-1) or skipOrInclude(SUM+nums[i], i-1)

            cache[(SUM,i)] = state

            return state
        
        return skipOrInclude(0,len(nums)-1)