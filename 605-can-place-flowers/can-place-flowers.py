class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n==0:
            return True
        count = 0
        if len(flowerbed)==1:
            if flowerbed[0]==0:
                    count+=1
                    if count==n:
                        return True
            return False
        if flowerbed[0]==0 and flowerbed[1]==0:
            count += 1
            if count == n:
                return True
            flowerbed[0] = 1
        if flowerbed[-1]==0 and flowerbed[-2]==0:
            count += 1
            if count == n:
                return True
            flowerbed[-1] = 1
        for x in range(1,len(flowerbed)-1):
            if flowerbed[x]==0:
                if flowerbed[x-1]==0 and flowerbed[x+1]==0:
                    count+=1
                    if count==n:
                        return True
                    flowerbed[x]=1
        return False