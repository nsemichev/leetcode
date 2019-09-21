class Solution(object):
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        partitions = []
        cur_letters = []
        count = 1
        for i in range(len(S)):
            letter = S[i]
            if letter not in S[i+1:]:
                inv = False
                for l in cur_letters:
                    if l in S[i+1:]:
                        inv = True
                        break
                if not inv:
                    partitions.append(count)
                    count = 1
                    cur_letters = []
                    continue
            
            count += 1
            if letter not in cur_letters:
                cur_letters.append(letter)
        return partitions
