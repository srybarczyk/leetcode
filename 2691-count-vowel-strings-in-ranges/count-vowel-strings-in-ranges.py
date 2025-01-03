class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowels = {"a","e","i","o","u"}
        TrueCount = 0
        ResultsArray=[]
        print ((ResultsArray))


        for ind, val in enumerate (words):
            bool = False
            if (val[0]) in vowels:
                if (val[-1]) in vowels:
                    bool=True

            ResultsArray.append(TrueCount)
            if bool == True:
                TrueCount += 1
        ResultsArray.append(TrueCount)

        ANS=[]
        for query in queries:
            ANS.append(ResultsArray[query[1]+1]-ResultsArray[query[0]])
        return ANS