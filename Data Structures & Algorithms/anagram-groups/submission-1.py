class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dictionary of anagrams, categorize words based on anagram
        dict_anagram = defaultdict(list)

        for s in strs:
            
            # Keeps track of char count where index is based on alphabetical order
            # e.g. index 0 is a, index 1 is b, etc...
            count = [0] * 26

            for c in s:
                count[ord(c) - ord('a')] += 1
            
            # Categorize word into their correct anagram based on character count
            dict_anagram[tuple(count)].append(s)
            
        return list(dict_anagram.values())
