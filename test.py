from bisect import bisect_left, bisect_right
from typing import List, Optional

class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = list(zip(difficulty, profit))
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

if __name__=="__main__":

    difficulty = [68,35,52,47,86]
    profit = [67,17,1,81,3]
    worker = [92,10,85,84,82]

    print(Solution().maxProfitAssignment(difficulty=difficulty,profit=profit,worker=worker))