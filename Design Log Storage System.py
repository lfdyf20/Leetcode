class LogSystem(object):

    def __init__(self):
        self.logs = []


    def put(self, tid, timestamp):
        """
        :type id: int
        :type timestamp: str
        :rtype: void
        """
        self.logs.append((tid, timestamp))
        

    def retrieve(self, s, e, gra):
        """
        :type s: str
        :type e: str
        :type gra: str
        :rtype: List[int]
        """
        index = {'Year': 5, 'Month': 8, 'Day': 11, 
                 'Hour': 14, 'Minute': 17, 'Second': 20}[gra]
        start = s[:index]
        end = e[:index]
        return [ tid for tid, timestamp in self.logs if start <= timestamp[:index] <= end ]


# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(s,e,gra)