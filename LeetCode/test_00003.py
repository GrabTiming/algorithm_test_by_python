# coding = utf-8
#!/usr/bin/env python

"""
322 零钱兑换
https://leetcode.cn/problems/coin-change/description/

思路：简单的完全背包,每种元素都有无数个
"""
from typing import List, Dict


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        mx = 1<<20
        dp :List[int] = [mx for i in range(amount+1)]
        dp[0] = 0
        for coin in  coins:
            for  j in range(coin,amount+1):

                dp[j] = min(dp[j],dp[j-coin]+1)

        return dp[amount] if dp[amount] !=mx else -1

if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    solution = Solution()
    print(solution.coinChange(coins,amount))