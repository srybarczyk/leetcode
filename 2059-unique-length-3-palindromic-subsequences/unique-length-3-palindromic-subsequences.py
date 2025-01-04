class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        lettersset=set(s)
        ans=0
        for letter in lettersset:
            firstindex, lastindex = (s.index(letter),s.rindex(letter))
            betweenset=set()
            for betweenletters in range(firstindex+1,lastindex):
                betweenset.add(s[betweenletters])
            ans+=len(betweenset)
        return ans