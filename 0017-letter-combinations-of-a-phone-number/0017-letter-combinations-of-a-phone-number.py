class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        if not digits:
            return []

        letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        combinations = [""]

        for digit in digits:
            combinations = [
                prefix + letter
                for prefix in combinations
                for letter in letters[digit]
            ]

        return combinations