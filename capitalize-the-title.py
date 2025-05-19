class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        a=""
        for i in title.split():
            if len(i)>2:
                b=i.lower().title()
                b=b
                a=a+b+" "
            else:
                c=i.lower()
                a=a+c+" "
        return a.strip()