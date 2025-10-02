class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
        if sum(nums)%2!=0:
            return False

        half_sum = sum(nums)//2
        table = [ [ False for i in range(half_sum+1) ] for _ in range(len(nums))]

        for i in range(len(nums)):
            table[i][0] = True

        for i in range(len(nums)):
            for j in range(half_sum+1):

                if (j - nums[i])<0:
                    table[i][j] = table[i-1][j]
                else:
                    table[i][j] = table[i-1][j-nums[i]] or table[i-1][j]

        return table[-1][-1]