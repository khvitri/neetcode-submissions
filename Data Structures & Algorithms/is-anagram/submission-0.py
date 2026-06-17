class Solution:

    def _countLetters(self, word: str) -> Dict[str, int]:
        """Count occurances of each letter."""
        count: Dict[str, int] = dict()

        for c in word:
            count.setdefault(c, 0)
            count[c] += 1
        
        return count

    def isAnagram(self, s: str, t: str) -> bool:
        sWordCount: Dict[str, int] = self._countLetters(s)
        tWordCount: Dict[str, int] = self._countLetters(t)

        return sWordCount == tWordCount
