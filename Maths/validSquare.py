class Solution:
    def vectorize(self, p1, p2):
        return [p2[0]-p1[0], p2[1]-p1[1]]
    
    def distanceMeasure(self,v):
        return v[0]**2 + v[1]**2
    
    def dot(self,v1, v2):
        return (v1[0])*(v2[0])+(v1[1])*(v2[1])
    
    def validSquare(self, p1, p2, p3, p4) -> bool:
        vectorList = []
        vectorList.append([p1[1]-p2[1],p1[0]-p2[0]])
        vectorList.append([p1[1]-p3[1],p1[0]-p3[0]])
        vectorList.append([p1[1]-p4[1],p1[0]-p4[0]])
        vectorList.append([p2[1]-p3[1],p2[0]-p3[0]])
        vectorList.append([p2[1]-p4[1],p2[0]-p4[0]])
        vectorList.append([p3[1]-p4[1],p3[0]-p4[0]])