class Solution(object):
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        s = S
        for letter in J: 
            s = s.replace(letter, "")
        return len(S) - len(s)
