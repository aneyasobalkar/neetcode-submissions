class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        def neighbors(lock):
            res = []
            for i in range(4):
                minusChar = str((int(lock[i]) - 1 + 10) % 10)
                extraChar = str((int(lock[i]) +1) % 10)
                res.append(lock[:i] + minusChar + lock[i+1:])
                res.append(lock[:i] + extraChar + lock[i+1:])
            return res
        q = deque([["0000", 0]])
        visited = set(deadends)
        while q:
            lock, level = q.popleft()
            if lock == target:
                return level 
            for c in neighbors(lock):
                if c not in visited:
                    visited.add(c)
                    q.append([c, level + 1])
        return -1
                
        
