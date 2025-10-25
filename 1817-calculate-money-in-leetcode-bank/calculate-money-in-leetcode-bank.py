class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7
        days = n % 7
        money = 0
        for i in range(weeks):
            money += sum(range(i + 1, i + 8))
        money += sum(range(1 + weeks, 1 + weeks + days))
        return money

