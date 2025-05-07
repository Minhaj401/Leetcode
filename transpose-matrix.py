class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        rows = len(matrix)
        columns = len(matrix[0])
        mat=[[0 for _ in range(rows) ] for _ in range(columns)]
        for i in range(columns):
            for j in range(rows):
                mat[i][j]=matrix[j][i]

        return mat