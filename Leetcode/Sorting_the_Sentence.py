class Solution:
    def sortSentence(self, s: str) -> str:
        words = s.split()
        sorted_words = [None] * len(words)
        for word in words:
            position = int(word[-1]) - 1
            sorted_words[position] = word[:-1]
        result = ''

        for i in range(len(sorted_words)):
            if i == 0:
                result += sorted_words[i]
            else:
                result += ' ' + sorted_words[i]

        return result


res = Solution()
s = "is2 sentence4 This1 a3"
print(res.sortSentence(s))
