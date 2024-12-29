def searchMatrix(matrix, target):
    if not matrix or not matrix[0]:  # Check for empty matrix
        return False

    rows, cols = len(matrix), len(matrix[0])
    row, col = 0, cols - 1  # Start at the top-right corner

    while row < rows and col >= 0:
        current = matrix[row][col]
        if current == target:
            return True  # Target found
        elif current > target:
            col -= 1  # Move left
        else:
            row += 1  # Move down

    return False  # Target not found

# Test the function
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]
target = 6

print(searchMatrix(matrix, target))  # Output: True
