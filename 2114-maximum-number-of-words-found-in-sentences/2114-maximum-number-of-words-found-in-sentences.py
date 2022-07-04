class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        
        res = 0
        
        for item in sentences:
            space = 0
            space = item.count(" ")
            
            if res < space + 1:
                res = space + 1
        
        return res