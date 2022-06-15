class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        location = []
        for i in matrix:
            if 0 in i:
                place = 0
                for j in i:
                    if j == 0:
                        location.append(place)
                    place += 1
                    matrix[matrix.index(i)][i.index(j)] = 0

        for i in location:
            for j in matrix:
                matrix[matrix.index(j)][i] = 0
