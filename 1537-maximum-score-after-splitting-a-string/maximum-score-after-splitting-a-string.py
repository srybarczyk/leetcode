class Solution:
    def maxScore(self, s: str) -> int:
        sright=s
        loop=1
        maxscore=0
        while len(sright) >1:
            sleft=s[:loop]
            sright=sright[-(len(sright)-1):]
            leftscore=sleft.count('0')
            rightscore=sright.count('1')
            totalscore=leftscore+rightscore
            if totalscore>maxscore:
                maxscore=totalscore

            loop +=1
            if loop >len(s)+1:
                break
        return maxscore