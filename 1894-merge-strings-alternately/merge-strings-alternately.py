class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        result = []
        n1, n2 = len(word1), len(word2)
        
        # Iterate up to the maximum length of both strings
        for i in range(max(n1, n2)):
            if i < n1:
                result.append(word1[i])
            if i < n2:
                result.append(word2[i])
                
        return "".join(result)