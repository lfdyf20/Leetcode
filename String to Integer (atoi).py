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
        


str = "1"
sample = Solution()
print(sample.myAtoi(str))
