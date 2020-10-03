# %% [933. Number of Recent Calls](https://leetcode.com/problems/number-of-recent-calls/)
class RecentCounter:
    def __init__(self):
        self.deque = collections.deque()

    def ping(self, t: int) -> int:
        self.deque.append(t)
        while self.deque[0] < t - 3000:
            self.deque.popleft()
        return len(self.deque)
