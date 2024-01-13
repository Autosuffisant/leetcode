class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sLetters = dict()
        tLetters = dict()

        for letter in s:
            sLetters[letter] = sLetters.get(letter, 0) + 1

        for letter in t:
            tLetters[letter] = tLetters.get(letter, 0) + 1

        for letter in "abcdefghijklmnopqrstuvwxyz":
            sOccurence = sLetters.get(letter, 0)
            tOccurence = tLetters.get(letter, 0)

            if sOccurence > tOccurence:
                sLetters[letter] = sOccurence - tOccurence
            else:
                sLetters[letter] = 0

        return sum(sLetters.values())