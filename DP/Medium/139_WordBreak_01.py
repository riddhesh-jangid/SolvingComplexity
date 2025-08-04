from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache(None)
        def make_recursion(stringLeft):

            if stringLeft=='':
                return True

            tof = False
            for word in wordDict:
                if stringLeft.startswith(word):
                    newStartIndex = len(word)
                    tof = tof or make_recursion( stringLeft[newStartIndex:] )
            
            return tof

        return make_recursion(s)
        