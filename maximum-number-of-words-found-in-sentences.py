class Solution(object):
    def mostWordsFound(self, sentences):
        """
        :type sentences: List[str]
        :rtype: int
        """
        max=0
        for i in sentences:
            list=[a for a in i.split()]
            if len(list)>max:
                max=len(list)
        return max