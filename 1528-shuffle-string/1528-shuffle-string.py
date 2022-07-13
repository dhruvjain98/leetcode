class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        
        res = [''] * len(indices)
        for i in range(0, len(indices)):
            res[indices[i]] = s[i]
        
        out = "" 
        return(out.join(res))