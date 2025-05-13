class Solution(object):
    def interpret(self, command):
        """
        :type command: str
        :rtype: str
        """
        a=command.replace("()","o")
        a=a.replace("(al)","al")
        return a
        