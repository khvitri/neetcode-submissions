class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        ROWS = len(words)
        for word_num in range(ROWS):
            for char_pos in range(len(words[word_num])):
                if (char_pos >= ROWS or
                    word_num >= len(words[char_pos]) or
                    words[word_num][char_pos] != words[char_pos][word_num]):
                    return False
        
        return True

