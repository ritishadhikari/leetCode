class Solution(object):
    def countSquares(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """

        m,n = len(matrix[0]), len(matrix)
        ans = 0
        for i in range(n-1,-1,-1):
            for j in range(m-1, -1, -1):
                if i+1 < n and j+1 < m and matrix[i][j] == 1:
                    matrix[i][j] = min(matrix[i+1][j], matrix[i][j+1], matrix[i+1][j+1]) + 1
            ans += sum(matrix[i])
        return ans


if __name__=="__main__":
    matrix=[
            [0,1,1,1],
            [1,1,1,1],
            [0,1,1,1]
            ]
    print(Solution().countSquares(matrix=matrix))