class Solution:
    def countPrefixSuffixPairs(self, words: list[str]) -> int:
        ans=0
        n=len(words)
        string_lengths=[len(words[x]) for x in range (n)]
        for x in range (n):
            for y in range(n):
                if x>y:
                    if string_lengths[x]>=string_lengths[y]:
                        if words[y]==(words[x])[-string_lengths[y]:]:
                            if words[y]==(words[x])[:string_lengths[y]]:
                                ans+=1
        return ans