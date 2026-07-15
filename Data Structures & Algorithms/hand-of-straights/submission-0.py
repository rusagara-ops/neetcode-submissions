
from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        
        if len(hand) % groupSize != 0:
            return False

        frequencymap = Counter(hand)
        hand.sort()

        for num in hand:
            if frequencymap[num] == 0:
                continue
            else:
                start = num
                for i in range(start, start+groupSize):
                    if not frequencymap[i]:
                        return False
                    else:
                        frequencymap[i] -= 1

        return True

        
            

    
        

            
            


            