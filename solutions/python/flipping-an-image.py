class Solution(object):
    def flipAndInvertImage(self, A):
        """
        :type A: List[List[int]]
        :rtype: List[List[int]]
        """
        B = []
        for i in range(len(A)):
            new_row = A[i][::-1]
            for i in range(len(new_row)):
                if new_row[i] == 0:
                    new_row[i] = 1
                else:
                    new_row[i] = 0
            B.append(new_row)
        return B
