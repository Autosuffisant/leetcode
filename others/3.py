class Solution:
    # Hideous, yet functional first attempt
    def lengthOfLongestSubstring(self, s: str) -> int:
        sList = list(s)
        sLen = len(s)
        currentIndex = 0
        longest = 0
        currentWord = ""
        letters = {}

        while currentIndex < sLen:
            # print(sList[currentIndex:])
            for letter in sList[currentIndex:]:
                # print(letter)
                if letter in letters:
                    # print(letter + " is in")
                    if len(currentWord) > longest:
                        longest = len(currentWord)
                        # print(longest)
                    letters.clear()
                    currentWord = ""
                    break
                else:
                    letters[letter] = letter
                    currentWord = currentWord + letter
            currentIndex = currentIndex + 1

        if len(currentWord) > longest:
            return len(currentWord)

        return longest


# Best solution from leetcode
# TODO: Understand it's logic
class BestSolution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        start = result = 0
        seen = dict()

        for i, c in enumerate(s):

            if seen.get(c, -1) >= start:
                start = seen[c] + 1

            result = max(result, i - start + 1)
            seen[c] = i

        return result
