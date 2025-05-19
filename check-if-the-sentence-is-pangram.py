class Solution(object):
    def checkIfPangram(self, sentence):
        """
        :type sentence: str
        :rtype: bool
        """
        a=[]
        for i in sentence:
            a.append(i)
        alpha=["a","s","d","f","g","h","j","k","l","q","w","e","r","t","y","u","i","o",'p','z','x','c','v','b','n','m']
        
        for i in alpha:
            if i not in a:
                return False
        return True