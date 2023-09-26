# Function to calculate the sum of a row in the matrix
row_sum = lambda row: sum(row)

# Function to sort a matrix based on the sum of its rows
def sort_matrix_by_row_sum(matrix):
    return sorted(matrix, key=row_sum)

# Test cases
matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# Sort and print the matrices based on row sums
sorted_matrix1 = sort_matrix_by_row_sum(matrix1)
sorted_matrix2 = sort_matrix_by_row_sum(matrix2)

print("Original Matrix:")
for row in matrix1:
    print(row)

print("Sort the matrix in ascending order according to the sum of its rows:")
for row in sorted_matrix1:
    print(row)

print("\nOriginal Matrix:")
for row in matrix2:
    print(row)

print("Sort the matrix in ascending order according to the sum of its rows:")
for row in sorted_matrix2:
    print(row)
