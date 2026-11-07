class Solution:

  def generateMatrix(self, n: int) -> list[list[int]]:
    matrix = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1

    while top <= bottom and left <= right:
      # Traverse from left to right across the top row
      for col in range(left, right + 1):
        matrix[top][col] = num
        num += 1
      top += 1

      # Traverse downward along the right column
      for row in range(top, bottom + 1):
        matrix[row][right] = num
        num += 1
      right -= 1

      # Traverse from right to left across the bottom row
      if top <= bottom:
        for col in range(right, left - 1, -1):
          matrix[bottom][col] = num
          num += 1
        bottom -= 1

      # Traverse upward along the left column
      if left <= right:
        for row in range(bottom, top - 1, -1):
          matrix[row][left] = num
          num += 1
        left += 1

    return matrix