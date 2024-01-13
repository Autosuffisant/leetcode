class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sLetters = dict()
        tLetters = dict()

        for letter in s:
            if not sLetters.get(letter):
                sLetters[letter] = 0
            sLetters[letter] = sLetters[letter] + 1

        for letter in t:
            if not tLetters.get(letter):
                tLetters[letter] = 0
            tLetters[letter] = tLetters[letter] + 1

        for letter in "abcdefghijklmnopqrstuvwxyz":
            sOccurence = sLetters.get(letter) or 0
            tOccurence = tLetters.get(letter) or 0
            if sOccurence > tOccurence:
                # Change the letter in the string to match the same occurence
                s = s.replace(letter, "", sOccurence - tOccurence)
            elif tOccurence > sOccurence:
                # Add the letter to the string to match the same occurence
                s = s.replace(letter, letter * (tOccurence - sOccurence))

        return 0