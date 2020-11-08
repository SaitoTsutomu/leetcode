# %% [1185. Day of the Week](https://leetcode.com/problems/day-of-the-week/)
# 問題：曜日を返せ
# 解法：%Aを用いる
class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        return f"{datetime.date(year, month, day):%A}"
