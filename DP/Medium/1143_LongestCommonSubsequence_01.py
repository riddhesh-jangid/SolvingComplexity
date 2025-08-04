from functools import lru_cache

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        @lru_cache(None)
        def make_recursion(i, j):

            if i<0 or j<0:
                return 0

            if text1[i] == text2[j]:
                return 1 + make_recursion(i-1, j-1)
            else:
                # make choices
                skip_text1 = make_recursion(i-1, j)
                skip_text2 = make_recursion(i, j-1)
                return skip_text1 if skip_text1 > skip_text2 else skip_text2 


        return make_recursion(len(text1)-1, len(text2)-1)