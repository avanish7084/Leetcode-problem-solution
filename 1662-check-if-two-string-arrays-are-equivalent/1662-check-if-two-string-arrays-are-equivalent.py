class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        temp1,temp2="",""
        for char in word1:
            temp1+=char
        for char in word2:
            temp2+=char
        if temp1==temp2:
            return True
        return False