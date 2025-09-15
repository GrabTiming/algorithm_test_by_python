# coding = utf-8
#!/usr/bin/env python

"""
518. 零钱兑换 II
https://leetcode.cn/problems/coin-change-ii/description/

思路：
背包问题的方案数问题，达到某个要求有多少种方法或路径
len(coins) <=300
amount <= 5000

"""
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp :List[int] = [0 for i in range(amount+1)]

        dp[0] = 1
        for coin in coins:
            for j in range(coin,amount+1):
                dp[j] = dp[j] + dp[j-coin]

        return dp[amount]

if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 5
    print(s.change(amount,coins)
    )


