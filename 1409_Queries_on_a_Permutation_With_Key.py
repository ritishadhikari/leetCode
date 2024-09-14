from typing import List
class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        array=[i+1 for i in range(0,m)]
        result=[]
        for i in range(len(queries)):
            v=queries[i]
            result.append(array.index(v))
            array.remove(v)
            array.insert(0,v)
        return result


if __name__=="__main__":
    queries = [7,5,5,8,3]
    m = 8
    print(Solution().processQueries(queries=queries,m=m))