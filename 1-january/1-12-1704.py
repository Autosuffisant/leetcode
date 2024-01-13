class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        sList = list(s.lower())
        sLen = len(sList)

        s1 = sList[:sLen // 2]
        s2 = sList[sLen // 2:]

        v1 = sum([1 for c in s1 if c in 'aeiou'])
        v2 = sum([1 for c in s2 if c in 'aeiou'])

        return v1 == v2