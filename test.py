class Solution:
    def findClosestElements(self, A, k, x):
        left, right = 0, len(A) - k
        while left < right:
            mid = (left + right) // 2
            if x - A[mid] > A[mid + k] - x:
                left = mid + 1
            else:
                right = mid-1
        return A[left:left + k]


if __name__=="__main__":
    # A = [1,1,1,1,2,2,2,4,4,4,4,5,6]
    # k=4
    # x=5

    A=[0,2,2,3,4,6,7,8,9,9]
    k=4
    x=5
    print(Solution().findClosestElements(A=A,k=k,x=x))
