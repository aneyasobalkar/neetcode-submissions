class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        q = deque([0])
        farthest = 0
        while q:
            i = q.popleft()
            start = max(farthest+1, i+minJump)
            end = min(len(s), i+maxJump+1)
            for j in range(start, end):
                if s[j] == "0":
                    q.append(j)
                    if j == len(s) -1:
                        return True
            farthest = i+maxJump
        return False