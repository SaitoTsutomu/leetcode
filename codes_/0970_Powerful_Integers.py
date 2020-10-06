# %% [970. Powerful Integers](https://leetcode.com/problems/powerful-integers/)
# 問題：bound以下でx**i+y**jとなる数を返せ
# 解法：i, jの上限内で繰り返す
class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        ans = set()
        nx = 0 if x == 1 else int(math.log(bound - 1, x))
        ny = 0 if y == 1 else int(math.log(bound - 1, y))
        for i in range(nx + 1):
            for j in range(ny + 1):
                if (v := x ** i + y ** j) > bound:
                    break
                ans.add(v)
        return list(ans)


def dfs(tn, v):
    return not tn or tn.val == v and dfs(tn.left, v) and dfs(tn.right, v)
