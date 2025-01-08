class Solution:
    def stringMatching(self, words: list[str]) -> list[str]:
        word_set= set(words)
        ans=list(set(x for x in word_set for y in word_set if x != y and x in y))
        return ans