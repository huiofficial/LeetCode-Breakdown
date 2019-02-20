# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def insert(self, intervals: 'List[Interval]', newInterval: 'Interval') -> 'List[Interval]':
        intervals.append(newInterval)
        intervals = sorted(intervals, key=lambda x: x.start)

        head = intervals[0].start
        tail = intervals[0].end
        result = []

        for i in range(1, len(intervals)):
            currentInterval = intervals[i]
            if tail >= currentInterval.start:
                tail = max(tail, currentInterval.end)
            else:
                result.append([head, tail])
                head = currentInterval.start
                tail = currentInterval.end

        result.append([head, tail])
        return result
