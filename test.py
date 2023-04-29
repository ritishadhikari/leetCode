from collections import deque
class Solution:
    def canFinish(self, n, pres):
        ind = [[] for _ in range(n)]  # indegree
        oud = [0] * n  # outdegree
        for p in pres:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = deque()
        for i in range(n):
            if oud[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.popleft()
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        return k == n


if __name__=="__main__":
    # n=5
    # pres=[[2,1],[0,1],[1,4],[2,3],[2,4]]
    n=2
    pres=[[1,0],[0,1]]
    print(Solution().canFinish(n=n,pres=pres))