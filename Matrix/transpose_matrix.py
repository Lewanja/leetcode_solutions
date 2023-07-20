# Given a 2D integer array matrix, return the transpose of matrix.
#
# The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
matrix = [[1,2,3],[4,5,6],[7,8,9]]
length_of_matrix, length_of_first_row = len(matrix), len(matrix[0])

ans = [[None] * length_of_matrix for index in range (length_of_first_row)]

for row_index in range(length_of_matrix):
    for column_index in range(length_of_first_row):
        ans[column_index][row_index] = matrix[row_index][column_index]

print(ans)






# transpose_matrix = []
# new_matrix = []

# for row in range(0, len(matrix)-1):
#     row_matrix = []
#     column = 0
#     while column <= len(matrix):
#         new_value = matrix[column][row]
#         row_matrix.append(new_value)
#         column += 1
#     new_matrix.append(row_matrix)
# print(new_matrix)
