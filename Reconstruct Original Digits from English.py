from collections import Counter
class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        ct = Counter( s )
        res = ""

        six = ct["x"]
        ct["x"] = 0
        ct["s"] -= six
        ct["i"] -= six
        res += "6" * six

        seven = ct["s"]
        ct["s"] = 0
        ct["e"] -= seven * 2
        ct["v"] -= seven
        ct["n"] -= seven
        res += "7"*seven

        five = ct["v"]
        ct["v"] = 0
        ct["f"] -= five
        ct["i"] -= five
        ct["e"] -= five
        res += "5" * five

        four = ct["u"]
        ct["u"] = 0
        ct["o"] -= four
        ct["f"] -= four
        ct["r"] -= four
        res += "4" * four

        two = ct['w']
        ct['w'] = 0
        ct['t'] -= two
        ct['o'] -= two
        res += "2" * two

        zero = ct['z']
        ct['z'] = 0
        ct['e'] -= zero
        ct['r'] -= zero
        ct['o'] -= zero
        res += "0" * zero

        three = ct["r"]
        res += "3" * three

        one = ct["o"]
        res += "1" * one

        eight = ct['g']
        ct['i'] -= eight
        res += "8" * eight

        nine = ct['i']
        res += "9" * nine

        
        return "".join(sorted(res))







s = "fviefuro"

sl = Solution()
print( sl.originalDigits( s ) )