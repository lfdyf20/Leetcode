class Solution(object):
    def computeArea(self, A, B, C, D, E, F, G, H):
        """
        :type A: int
        :type B: int
        :type C: int
        :type D: int
        :type E: int
        :type F: int
        :type G: int
        :type H: int
        :rtype: int
        """
        # print A,B,C,D,E,F,G,H
        # if (C-G)*(G-H)<0:
        #     maxh = max(D,H)
        #     minh = min(B,F)
        #     maxw = max(C,G)
        #     minw = min(A,E)
        #     print 'maxh=',maxh,'minh=',minh,'maxw=',maxw,'minw=',minw
        #     total = (maxh-minh)*(maxw-minw)
        #     print 'total=',total
        #     cut1 = ( max(A,E) - min(A,E) )*( max(B,F) - min(B,F) )
        #     cut2 = ( max(C,G) - min(C,G) )*( max(D,H) - min(D,H) )
        #     total = total - cut1 - cut2
        #     return total
        # else:
        #     return self.computeArea(C,B,A,D,E,H,G,F)
        total = (C - A) * (D - B) + (G - E) * (H - F)

        width = max(0, min(C, G) - max(A, E))
        height = max(0, min(D, H) - max(B, F))

        return total - width * height


        
        return area1+area2


solution = Solution()
print solution.computeArea(-2,-2,2,2,1,-3,3,-1)
