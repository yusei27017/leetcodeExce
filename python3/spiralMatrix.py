class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
            # 取得列數 橫向 m
            colLength = len(matrix)
            # 取得行數 縱向 n
            rowLength = len(matrix[0])
            # 設定初始出發方向
            vector = "right"
            # 初始化解答array
            ans = []
            # 設定邊界每當只要遍歷過，矩陣形狀會改變
            left, top = 0, 0

            # 只要ans數量達到n*m就全部遍歷完成，跳出迴圈
            while len(ans) < len(matrix) * len(matrix[0]):
                # 用四個開關來判斷當前行走方向
                if vector == "right":
                    # 開始遍利寫入數值，範圍是左邊界至總行數
                    for i in range(left, rowLength):
                        ans.append(matrix[top][i])
                    # 遍歷完成後，最上面那列就用不到了故加一
                    top += 1
                    # 最後更改行走方向，從頭來過。
                    vector = "down"

                elif vector == "down":
                    for i in range(top, colLength):
                        # 開始遍利寫入數值，範圍是上邊界至總列數
                        ans.append(matrix[i][rowLength-1])
                    # 最左邊以遍歷完成，故行數減一
                    rowLength -= 1
    
                    vector = "left"

                elif vector == "left":
                    for i in range(rowLength-1, left-1, -1):
                        # 開始遍利寫入數值，範圍是總行數至左邊邊界
                        ans.append(matrix[colLength-1][i])
                    # 最下列遍歷完成故列數減一
                    colLength -= 1
                    # 再次更變方向重新循環
                    vector = "up"

                elif vector == "up":
                    for i in range(colLength-1, top-1, -1):
                        # 開始遍利寫入數值，範圍是總列數至上邊邊界
                        ans.append(matrix[i][left])
                    # 最左邊行已遍歷完成，左邊邊界推進一格
                    left += 1

                    vector = "right"
            # 全部數字遍歷完成回傳答案
            return ans
