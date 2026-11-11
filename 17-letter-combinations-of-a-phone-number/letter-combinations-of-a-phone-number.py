class Solution:

  def letterCombinations(self, digits: str) -> list[str]:
    if not digits:
      return []

    phone_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }

    result = []

    def backtrack(index, current_path):
      if index == len(digits):
        result.append("".join(current_path))
        return

      for char in phone_map[digits[index]]:
        current_path.append(char)
        backtrack(index + 1, current_path)
        current_path.pop()

    backtrack(0, [])
    return result