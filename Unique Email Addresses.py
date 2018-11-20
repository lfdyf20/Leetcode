class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        res = set()
        for email in emails:
        	localname, hostname = email.split("@")
        	localname = localname.split("+")[0]
        	localname = localname.replace(".", "")
        	res.add(localname+"@"+hostname)
        return len(res)



emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

sl = Solution()
print( sl.numUniqueEmails( emails ) )