class Solution:
    def countPoints(self, points: List[List[int]], queries: List[List[int]]) -> List[int]:
        
        answer = []
        
        for circ in queries:
            # print("Circle: {}".format(circ))
            cnt = 0
            for pts in points:
                # print("Pt: {}".format(pts))
                # dist = int(math.sqrt((pts[0] - circ[0])**2 + (pts[1] - circ[1])**2))
                dist = (pts[0] - circ[0])**2 + (pts[1] - circ[1])**2
                # print("dist: ", dist)
                if dist <= circ[2]**2:
                    # print("add count for {}".format(pts))
                    cnt += 1
                
            answer.append(cnt)
            
        # print (answer)
        
        return answer