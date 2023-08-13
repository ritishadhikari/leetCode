from typing import List
class Solution:
    def calcEquation(self, 
                    equations: List[List[str]], 
                    values: List[float], 
                    queries: List[List[str]]) -> List[float]:
        tracker={}

        for i, (pre,post) in enumerate(equations):
            value=values[i]
            if pre not in tracker:
                tracker[pre]=set()
            if post not in tracker:
                tracker[post]=set()
            tracker[pre].add((post,value))
            tracker[post].add((pre,1/value))
 
            if len(pre)>1 or len(post)>1:
                indPre=set(pre).difference(post)
                indPost=set(post).difference(pre)
                if indPre and indPost:
                    indPre="".join(indPre)
                    indPost="".join(indPost)
                    if indPre not in tracker:
                        tracker[indPre]=set()
                    tracker[indPre].add((indPost,value))
                    if indPost not in tracker:
                        tracker[indPost]=set()
                    tracker[indPost].add((indPre,1/value))

        answer=[]
        for preq,postq in queries:
            trackerc=tracker.copy()
            temp=[]
            if preq not in trackerc or postq not in trackerc:
                answer.append(-1.0)
            elif preq in trackerc:
                initialequations=trackerc[preq]
                trackerc.pop(preq)
                for ie in initialequations:
                    temp.append(ie)
                while temp:
                    success=False
                    postqPot,val=temp.pop(0)
                    if postqPot==postq:
                        answer.append(val)
                        success=True
                        break
                    else:
                        if postqPot in trackerc:    
                            nextEquations=trackerc.get(postqPot)
                            trackerc.pop(postqPot)
                            for ne in nextEquations:
                                temp.insert(0,(ne[0],ne[1]*val))
                if success==False:
                    answer.append(-1)
        return answer




if __name__=="__main__":
    equations =  [["a","b"],["ab","c"],["a","bc"]]
    values = [2.0,3.0,4.0]
    queries = [["a","c"],["b","a"],["ab","c"],["a","a"],["x","x"]]
    print(
        Solution().calcEquation(
        equations=equations,
        values=values,
        queries=queries,
            )
        )