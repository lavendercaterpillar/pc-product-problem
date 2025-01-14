# Product Problem

Problem belonging to the post-classroom Mock Interview Question Repository.

## Problem Statement

We are interested in finding the largest product of a contiguous vertical or horizontal sequence of numbers in a grid.

Your function will be given two arguments, a list of lists of integers and a number of elements in a sequence to find the product of.

For example:

```py
grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
```

Because n = 3, our sequence must include exactly 3 factors. The three contiguous numbers that form the highest product are 99, 88, and 77, giving us a maximum product of 670824. Therefore, our function should return 670824.

Note that the numbers can be contiguous horizontally OR vertically. However, diagonal numbers will NOT be considered contiguous.

Inspired by https://projecteuler.net/problem=11

## Examples

### Example 1

```py
grid = [
    [1, 2,  3,  4,  5],
    [6, 7,  8,  9,  8],
    [1, 99, 88, 77, 5],
    [1, 2,  3,  4,  5],
    [1, 6,  7,  8,  9],
]
n = 3
largest_product(grid, n)
```

Produces

```py
670824  # 99 * 88 * 77
```

### Example 2

```py
grid = [
    [1, 2,  3,  4],
    [5, 6,  7,  8],
    [9, 10, 11, 12],
]
n = 3
largest_product(grid, n)
```

Produces

```py
1320  # 10 * 11 * 12
```

### Example 3

```py
grid = [
    [13, 0, 9],
    [2,  6, 10],
    [3,  7, 11],
    [4,  8, 12],
]
n = 3
largest_product(grid, n)
```

Produces

```py
1320  # 10 * 11 * 12
```

### Example 4

```py
grid = [
    [1, 99, 9],
    [2, 77, 10],
    [3, 22, 11],
    [4, 0,  12],
]
n = 2
largest_product(grid, n)
```

Produces

```py
7623  # 99 * 77
```

### Example 5

```py
grid = [
    [1, 2, 3],
    [4, 5, 6],
]
n = 3
largest_product(grid, n)
```

Produces

```py
120  # 4 * 5 * 6
```

### Example 6

```py
grid = [
    [-1],
    [2],
    [-3],
]
n = 2
largest_product(grid, n)
```

Produces

```py
-2  # -1 * 2
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: What should I do if the array is empty, or not big enough to fit the requested n?

A: You can assume the array will be large enough.

#### Q: What should I do if invalid input is passed in?

A: You can assume that the input will be valid.

#### Q: What should I do if n is less than 2?

A: You can assume that n will not be less than 2.

#### Q: Can there be a snaking path?

A: No, it must be a straight horizontal or vertical line of factors.

#### Q: What is a product? What is a factor?

A: A product is the result of multiplying numbers together. A factor is a number that is used to multiply. For example, in 2 \* 3 = 6, six is the product and two and three are factors.

### Hints

- If your candidate struggles with an initial algorithm, encourage them to walk through an example and describe how they would do it using only pen and paper

- If the candidate struggles with column-wise iteration, encourage them to focus on row-wise first. The first two test cases only require row-wise iteration.

- Out-of-bounds and off-by-one errors are super common here. If your candidate is getting frustrated by these, feel free to let them know that these are common issues to encounter, and even the question author made similar mistakes while building the sample solution!

## Optional Bonus At-Home Challenges

To be attempted after completing the interview.

- What is the time/space complexity of sample solution?

- Expand your solution so it can solve the original Project Euler version! https://projecteuler.net/problem=11 Feel free to explore other problems on this site. They're significantly more math-heavy than most interview questions, but they can be fun! The later problems also get SUPER HARD. There are some that the question author spent hours on and never successfully completed.
