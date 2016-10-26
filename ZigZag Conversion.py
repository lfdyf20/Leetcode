class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        # if numRows == 1:
        #     return s
        # # calculate period
        # p = 2*(numRows-1)

        # res = [""] * numRows
        # for i in range(len(s)):
        #     print("i=",i)
        #     floor = i%p
        #     print("floor is:",floor)
        #     if floor >= p/2:
        #         floor = p - floor
        #         print("here floor is: ",floor)
        #     res[floor] += s[i]
        #     print(res)
        # return "".join(res)
        ##-------------------
        # index = [ i for i in range(1, numRows+1)] + [ i*2 for i in range(1, numRows//2+1) ]
        # index = index * (len(s)//len(index)+1)
        # zigzag = []
        # for i,j in zip(index, s):
        #     zigzag.append((i,j))
        # zigzag.sort(key=lambda x:x[0])
        # print(zigzag)
        # res = list( map(lambda x:x[1], zigzag) )
        # res = "".join(res)
        # return res

        index = [ i for i in range(1, numRows+1)]
        index += index[1:-1][::-1]
        index = index * (len(s)//len(index)+1)
        zigzag = []
        for i,j in zip(index, s):
            zigzag.append((i,j))
        zigzag.sort(key=lambda x:x[0])
        # print(zigzag)
        res = list( map(lambda x:x[1], zigzag) )
        res = "".join(res)
        return res



s = "PAYPALISHIRING"
numRows = 5

s = "abc"
numRows = 2



sample = Solution()
print(sample.convert(s, numRows))

