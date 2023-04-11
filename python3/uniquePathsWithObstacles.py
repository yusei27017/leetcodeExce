class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)
        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1
        if obstacleGrid[0][0] == 1: return 0
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = 1
            else:
                dp[0][i] = 0
                break
        
        for j in range(1, m):
            if obstacleGrid[j][0] == 0:
                dp[j][0] = 1
            else:
                dp[j][0] = 0
                break

        for j in range(1, m):
            for i in range(1, n):
                if obstacleGrid[j][i] == 0:
                    dp[j][i] = dp[j][i-1] + dp[j-1][i]
                else:
                    dp[j][i] = 0

        return dp[-1][-1]