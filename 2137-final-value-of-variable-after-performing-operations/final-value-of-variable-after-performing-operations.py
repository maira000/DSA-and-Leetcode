class Solution(object):
    def finalValueAfterOperations(self, operations):
        x = 0
        for oper in operations:
            if "++" in oper:
                x +=1
            else:
                x -=1
        return x