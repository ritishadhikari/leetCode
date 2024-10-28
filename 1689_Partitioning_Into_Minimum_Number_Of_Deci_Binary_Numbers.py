class Solution:
    def minPartitions(self, n: str) -> int:
        return int(max(n))

if __name__=="__main__":
    n="32"
    print(Solution().minPartitions(n=n))