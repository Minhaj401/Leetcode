class Solution(object):
    def findDelayedArrivalTime(self, arrivalTime, delayedTime):
        """
        :type arrivalTime: int
        :type delayedTime: int
        :rtype: int
        """
        time=arrivalTime
        x=0
        while x!=delayedTime:
            time+=1
            x+=1
            if time==24:
                time=0
        return time