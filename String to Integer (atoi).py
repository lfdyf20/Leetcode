class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.lstrip()
        if str == "":
            return 0
        isNeg = 1
        res = ""
        if str[0] == "-":
            isNeg = -1
            for i in str[1:]:
                if i.isdigit():
                    res += i
                else:
                    break
        elif str[0] == "+":
            for i in str[1:]:
                if i.isdigit():
                    res += i
                else:
                    break
        else:
            for i in str:
                if i.isdigit():
                    res += i
                else:
                    break

        if res == "":
            return 0
        res = int(res) * isNeg
        if res >= 2147483647:
            return 2147483647
        if res <= -2147483648:
            return -2147483648
        return res

    def mySolution(self, str):
        try:
            while str[0] == " ":
                str = str[1:]
        except:
            return 0
        isPos = 1
        res = ""
        for i in str:
            if res == "" and i in "+-":
                res += i
                continue
            if i in "1234567890":               
                res +=  i
            else:
                break
        if (len(res)== 1 and res in "+-") or not res:
            return 0
        integer = int(res)
        return min(max(integer,-2147483648), 2147483647)






str = "abc"
sample = Solution()
print(sample.myAtoi(str))
print( sample.mySolution(str) )
