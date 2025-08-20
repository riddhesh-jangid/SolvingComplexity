class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        cols_count = len(text2)
        rows_count = len(text1)
        table = [[0 for _ in range(cols_count)] for _ in range(rows_count)]

        # Filling first row
        for j in range(cols_count):
            if text1[0] == text2[j]:
                table[0][j] = 1
            else:
                table[0][j] = max(table[0][j-1], 0)

        # Filling first col
        for i in range(rows_count):
            if text2[0] == text1[i]:
                table[i][0] = 1
            else:
                table[i][0] = max(table[i-1][0], 0)


        # Filling remaining table
        for i in range(1, rows_count):
            for j in range(1, cols_count):
                if text1[i] == text2[j]:
                    table[i][j] = table[i-1][j-1]+1
                else:
                    table[i][j] = max( table[i-1][j], table[i][j-1] )

        print(table)
        return table[-1][-1]