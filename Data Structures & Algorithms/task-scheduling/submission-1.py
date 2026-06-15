class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # create hashmap of task : frequency
        # max heap that sorts task by frequency
        # priority queue for inserting heap
        counts = Counter(tasks)
        maxHeap = list([-1*c for c in counts.values()])
        heapq.heapify(maxHeap)
        q = deque()
        times = 0
        while maxHeap or q:
            times += 1
            if not maxHeap:
                times = q[0][1]
            else:
                item = heapq.heappop(maxHeap) + 1
                if item:
                    q.append([item, times + n])
            if q:
                if q[0][1] == times:
                    item, _ = q.popleft()
                    heapq.heappush(maxHeap, item)
        return times 
