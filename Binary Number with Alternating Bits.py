class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        end = n % 2
        n //= 2
        while n:
            if n % 2 == end:
                return False
            end = n % 2
            n //= 2        
        return True
        



n = int("0101010101", 2)


sl = Solution()
print( sl.hasAlternatingBits( n ) )