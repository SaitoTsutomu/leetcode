# %% [1154. Day of the Year](https://leetcode.com/problems/day-of-the-year/)
# 問題：元旦からの日数を返せ
# 解法：datetime.datetime.timetuple().tm_ydayを用いる
class Solution:
    def dayOfYear(self, date: str) -> int:
        return datetime.datetime.strptime(date, "%Y-%m-%d").timetuple().tm_yday
