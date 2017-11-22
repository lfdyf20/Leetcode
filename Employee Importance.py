"""
# Employee info
"""
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates


class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        emps = { employee.id : employee for employee in employees }
        dfs = lambda id: sum( dfs(subId) for subId in emps[id].subordinates ) + emps[id].importance
        return dfs(id)

