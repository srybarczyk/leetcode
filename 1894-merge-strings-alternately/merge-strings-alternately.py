class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ans= ''.join([item for pair in zip(list(word1), list(word2))
                                 for item in pair])
        if len(word1)<len(word2):
            ans+=word2[len(word1)-len(word2):len(word2)]
        elif len(word1)>len(word2):
            ans+=word1[len(word2) - len(word1):len(word1)]
        return ans