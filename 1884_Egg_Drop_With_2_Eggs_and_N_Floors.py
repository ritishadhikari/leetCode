class Solution:
    # https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/discuss/1248560/Simple-Math-Problem-with-intuition-explained-O(1)-time-O(1)-space-or-Python
    def twoEggDrop(self, n: int) -> int:
        count=0
        decr=1
        while n>0:
            n-=decr
            count+=1
            decr+=1
        return count

if __name__=="__main__":
    n=105
    print(Solution().twoEggDrop(n=n))