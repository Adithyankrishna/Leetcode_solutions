from collections import Counter

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
    
        bull = 0
        cow = 0
        contains = Counter(secret)
        for i in range(len(secret)):
            if int(guess[i]) == int(secret[i]):
                bull+=1
                contains[secret[i]]-=1
        for i in range(len(guess)):

            if secret[i] != guess[i] and contains[guess[i]] > 0:
                contains[guess[i]]-=1
                
                cow+=1
        return f"{bull}A{cow}B"
            



        
        