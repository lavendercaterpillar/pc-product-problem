def largest_product(grid, n):
    max_product = None

    # Iterate row-wise
    for i in range(len(grid)):
        # Only go up to the nth to last item to avoid out-of-bounds
        for j in range(len(grid[0]) - n + 1):
            product = 1
            # Iterate over the n following items in the row
            for k in range(n):
                product *= grid[i][j+k]
            # Set the new max_product if we find a bigger one
            if max_product is None or product > max_product:
                max_product = product

    # Iterate column-wise
    for j in range(len(grid[0])):
        # Only go up to the nth to last item to avoid out-of-bounds
        for i in range(len(grid) - n + 1):
            product = 1
            # Iterate over the n following items in the column
            for k in range(n):
                product *= grid[i+k][j]
            # Set the new max_product if we find a bigger one
            if max_product is None or product > max_product:
                max_product = product

    return max_product


grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
expected = 670824  # 99 * 88 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12]
]
n = 3
expected = 1320  # 10 * 11 * 12
assert largest_product(grid, n) == expected

grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12]
]
n = 2
expected = 7623  # 99 * 77
assert largest_product(grid, n) == expected

grid = [
    [1, 2, 3],
    [4, 5, 6]
]
n = 3
expected = 120  # 4 * 5 * 6
assert largest_product(grid, n) == expected

grid = [
    [-1],
    [2],
    [-3]
]
n = 2
expected = -2  # -1 * 2
assert largest_product(grid, n) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
