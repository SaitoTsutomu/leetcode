# %% [937. Reorder Data in Log Files](https://leetcode.com/problems/reorder-data-in-log-files/)
class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        nod, dgt = [], []
        for log in logs:
            if log.split()[1].isnumeric():
                dgt.append(log)
            else:
                nod.append(log)
        nod.sort(key=lambda x: [" ".join((xx := x.split())[1:]), xx[0]])
        return nod + dgt
