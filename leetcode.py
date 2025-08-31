class Solution:
    def myAtoi(self, s: str) -> int:
        s =s.strip()
        if  len(s)== 0:  #to check is string is empty
            return 0
        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        else:
            sign = 1
        num = 0
        for i in s:
            if i.isdigit():
                num = num * 10 + int(i)
            else:
                break
        num *= sign
        if num <= -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        
        return num