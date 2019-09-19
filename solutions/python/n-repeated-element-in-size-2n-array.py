class Solution(object):
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        half = len(A)/2
        for i in range(0, half):
            if A[i] == A[half+i]:
                return A[i]
        if A[0] == A[1] or A[0] == A[half+1]:
            return A[0]
        if A[half] == A[half+1] or A[half] == A[1]:
            return A[half]
        
