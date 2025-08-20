from functools import lru_cache

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        if sum(nums)%2 != 0:
            return False
        
        targetSum = sum(nums)//2

        num_cols = targetSum+1
        num_rows = len(nums)

        # Constructing Table
        table = [ [False for _ in range(0,num_cols)] for _ in range(num_rows) ]
        
        # Setting up first row
        table[0][0] = True
        if nums[0] <= targetSum:
            table[0][ nums[0] ] = True

        # Filling the table
        for i in range(1, num_rows):

            for j in range(0, num_cols):

                # If upper is True make it True
                if table[i-1][j] == True:
                    table[i][j] = True

                if j >= nums[i]:
                    if table[i-1][j - nums[i]] == True:
                        table[i][j] = True

        return table[-1][-1]