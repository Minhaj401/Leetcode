class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        x,y,z=date.split("-")
        x=bin(int(x))
        x=x[2:]
        y=bin(int(y))
        y=y[2:]
        z=bin(int(z))
        z=z[2:]
        return x+"-"+y+"-"+z