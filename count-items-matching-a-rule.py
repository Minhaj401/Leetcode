class Solution(object):
    def countMatches(self, items, ruleKey, ruleValue):
        """
        :type items: List[List[str]]
        :type ruleKey: str
        :type ruleValue: str
        :rtype: int
        """
        count=0
        if ruleKey=="color":
            for i in items:
                if i[1]==ruleValue:
                    count+=1
        if ruleKey=="name":
            for i in items:
                if i[2]==ruleValue:
                    count+=1
        elif ruleKey=="type":
            for i in items:
                if i[0]==ruleValue:
                    count+=1
        return count