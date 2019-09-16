class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        alphabet = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        transformations = []
        for word in words:
            transform = ""
            for letter in word:
                transform += alphabet[ord(letter)-97]
            if transform not in transformations:
                transformations.append(transform)
        return len(transformations)
