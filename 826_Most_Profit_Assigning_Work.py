# VVI : Go with the Official Solution
# Official Solution below

from typing import List
class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        diff_prof=sorted(zip(difficulty,profit),key=lambda s:s[0])
        difficulty.sort()

        def getDiff(workerDiff,m):
            l=m
            r=len(difficulty)-1
            best=0
            while l<=r:
                m=(l+r)//2
                if workerDiff>difficulty[m]:
                    best=max(difficulty[m],best)
                    l=m+1
                elif workerDiff<difficulty[m]:
                    r=m-1
                else: return difficulty[m],m
            return best,l

        index=0
        p=0
        pp=0
        m=0
        for w in sorted(worker):
            bestDifficulty,m=getDiff(workerDiff=w,m=m)
            for diff,pr in diff_prof[index:]:
                if diff<=bestDifficulty:
                    pp=max(pr,pp)
                    index+=1
                else: break
            p+=pp
        return p

    '''
    class Solution(object):
    def maxProfitAssignment(self, difficulty, profit, worker):
        jobs = zip(difficulty, profit)
        jobs.sort()
        ans = i = best = 0
        for skill in sorted(worker):
            while i < len(jobs) and skill >= jobs[i][0]:
                best = max(best, jobs[i][1])
                i += 1
            ans += best
        return ans

    
    '''


if __name__=="__main__":
    difficulty = [2,4,6,8,10]
    profit = [10,20,30,40,50]
    worker = [4,5,6,7]
    print(Solution().\
        maxProfitAssignment(difficulty=difficulty,
                                    profit=profit,
                                    worker=worker))
