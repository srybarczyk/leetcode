import array as arr
import string

class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
       # alphabet=list(map(chr, range(97, 123)))
       # alphabet = dict.fromkeys(string.ascii_lowercase)
       # AlphaArray=arr.array('i')
       # AlphaArray = [(i for (i, x) in enumerate(alphabet) if letter == x) for letter in s]
       # for letter in s:
       #     for i, x in enumerate(alphabet):
       #         if letter==x:
       #             AlphaArray.append(i)
       # print (AlphaArray)
       # print (s)
       n=len(s)
       diff_array=[0]*n

       [self.ShiftForward(diff_array,shift,n) if shift[2]==1 else self.ShiftBackward(diff_array,shift,n) for shift in shifts]
       s_new=list(s)
       number_of_shifts=0
       # shifts_to_make=[]
       for i in range(n):
        #    number_of_shifts = 0
           number_of_shifts=(number_of_shifts+diff_array[i]) % 26
           if number_of_shifts<0:
               number_of_shifts+=26
           # shifts_to_make.append(number_of_shifts)
           s_new[i] = (chr((ord(s[i])-ord("a")+number_of_shifts)%26+ord("a")))


       # s_new=[alphabet[(x+y)%26] for x,y in zip(AlphaArray,shifts_to_make)]

       # for j in shifts_to_make:
       #      newletter = alphabet[(AlphaArray[j] + j) % 26]
       #          print (newletter)
            # s_new.append(newletter)
                # ans = ''.join(s_new)
           #
           # s_new=[(alphabet[(number_of_shifts+j)%26]) for j in AlphaArray]


       # for i in AlphaArray:
       #     # print(i)
       #     s_new.append(alphabet[i])
       ans=''.join(s_new)
       print(ans)
       return ans

    def ShiftForward(self,diff_array,shift,n):
        # DictAlpha = {AlphaArray}
        diff_array[shift[0]]+=1
        if shift[1]+1<n:
            diff_array[shift[1]+1]-=1

        # for i in range(shift[0],shift[1]+1):
        #     if AlphaArray[i] == 25:
        #         AlphaArray[i] = 0
        #     else:
        #         AlphaArray[i]+=1
        return
    def ShiftBackward(self,diff_array,shift,n):
        # DictAlpha = {AlphaArray}
        diff_array[shift[0]]-=1
        if shift[1]+1<n:
            diff_array[shift[1]+1]+=1
        # for i in range(shift[0],shift[1]+1):
        #     if AlphaArray[i] == -26:
        #         AlphaArray[i] = 25
        #     else:
        #         AlphaArray[i]-=1
        return