import heapq

# class PriorityQueue:

#     def __init__(self):
#         self._queue = []
#         self._index = 0

#     def push(self, item, priority):
#         heapq.heappush(self._queue, (-priority, self._index, item))
#         self._index += 1

#     def pop(self):
#         return heapq.heappop(self._queue)[-1]


class PriorityQueue():

    def __init__(self) -> None:
        self.queue = []
        self.index = 0

    def push(self, item, priority):
        heapq.heappush(self.queue, (-priority, self.index, item))
        self.index += 1

    def pop(self):
        return heapq.heappop(self.queue)[-1]


queue = PriorityQueue()
queue.push('foo', 1)
queue.push('bar', 5)
queue.push('spam', 4)
queue.push('grok', 1)
print(queue.pop())
print(queue.pop())
print(queue.pop())
"""
1.优先级队列 (-priority, self.index, item)) 中index的作用
"""
