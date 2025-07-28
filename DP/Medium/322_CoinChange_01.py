from functools import lru_cache

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        @lru_cache(None)
        def make_recursion(SUM, c):

            if SUM > amount or c<0:
                return -1

            if SUM == amount:
                return 0
            
            possibilities = [-1]

            # Left side 
            skip_coin = make_recursion(SUM, c-1)
            possibilities.append(skip_coin)

            # Right same coin side
            for i in range(1,10000):
                if SUM+(coins[c]*i) > amount:
                    break

                temp = make_recursion( SUM+(coins[c]*i), c)
                if temp!=-1:
                    possibilities.append( i + temp )
            
            possibilities = list(set(possibilities))
            possibilities.sort()
            if -1 in possibilities:
                possibilities.remove(-1)

            # if SUM==0 and c==0:
            #     print(f"sum {SUM} and coin {coins[c]} have {possibilities}")    
            # if SUM==10 and c==5:
            #     print(f"sum {SUM} and coin {coins[c]} have {possibilities}")    
            # if SUM==10 and c==2:
            #     print(f"sum {SUM} and coin {coins[c]} have {possibilities}")    
            # if SUM==10 and c==1:
            #     print(f"sum {SUM} and coin {coins[c]} have {possibilities}")    
            # if SUM==11 and c==1:
            #     print(f"sum {SUM} and coin {coins[c]} have {possibilities}")    

            if len(possibilities)==0:
                return -1

            if -1 in possibilities:
                possibilities.remove(-1)

            return min(possibilities)

        return make_recursion(0, len(coins)-1)