def largest_product(grid, n):
    # If I start my max_product at 1 or 0 then I'd have problem with negative products.
    # initiate it at negative infinity
    max_product = float('-inf')  

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            # Check horizontal (right)
            if col + n <= cols:
                row_product = 1
                for i in range(n):
                    row_product *= grid[row][col + i]
                max_product = max(max_product, row_product)

            # Check vertical (down)
            if row + n <= rows:
                col_product = 1
                for i in range(n):
                    col_product *= grid[row + i][col]
                max_product = max(max_product, col_product)

    return max_product

# ******************************
# ******** Refactoring *********
# ******************************
'''
    Repeated logic: Notice how the horizontal and vertical checks both involve:

        A bounds check

        A loop to calculate the product

        A call to max()

    → Can you extract that repeated pattern into a helper function?

    Loop structure: You're using for row in range(rows) and for col in range(cols), then checking directions.

    → Can you create a list of directions (e.g. right, down, diag) as (dx, dy) pairs and loop through those?

    Grid access: You often do grid[row + i][col + i].

    → Can you write a general get_product(start_row, start_col, dx, dy, n) function?

Let me know if you'd like a scaffold to start from — or you can try it and I'll review!
'''

# ******************************
# *********** Tests ************
# ******************************

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
print(largest_product(grid, n))
expected = -2  # -1 * 2
assert largest_product(grid, n) == expected

print("All tests passed!")
print("Discuss time & space complexity if time remains.")
