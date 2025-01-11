class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        gcd=""
        if len(str1)>len(str2):
            shorter_string=str2
            longer_string=str1
        else:
            shorter_string=str1
            longer_string = str2
        if len(longer_string)%len(shorter_string)==0:
            times_length=int(len(longer_string)/len(shorter_string))
            if shorter_string*times_length==longer_string:
                gcd=shorter_string
                return gcd
            print (times_length)
        for x in range(1,len(shorter_string)):
            temp_shorter_string=(shorter_string[:-x])
            if len(longer_string) % len(temp_shorter_string) == 0:
                times_length = int(len(longer_string) / len(temp_shorter_string))
                if temp_shorter_string * times_length == longer_string:
                    if len(shorter_string) % len(temp_shorter_string) == 0:
                        times_length = int(len(shorter_string) / len(temp_shorter_string))
                        if temp_shorter_string * times_length == shorter_string:
                            gcd = temp_shorter_string
                            return gcd
        return gcd