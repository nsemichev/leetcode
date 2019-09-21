class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        l = len(deck)
        if l == 1:
            return deck
        
        deck.sort()
        
        if l == 2:
            return deck    
        if l == 3:
            return [deck[0], deck[2], deck[1]]

        #firstHalf = deck[:(l+1)/2]
        newDeck = deck[(l+1)/2:]
        
        orderedDeck = self.deckRevealedIncreasing(newDeck)
        if l % 2 != 0:
            orderedDeck = orderedDeck[l/2-1:l/2] + orderedDeck[:l/2-1]
        combinedDeck = []
        for i in range(len(orderedDeck)):
            combinedDeck.append(deck[i])
            combinedDeck.append(orderedDeck[i])
        
        if l % 2 != 0:
            combinedDeck.append(deck[(l-1)/2])
            
        return combinedDeck
