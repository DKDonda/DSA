class Solution:
    def distanceMeasure(self,p1, p2):
        return (p1[0]-p2[0])**2 + (p1[1]-p2[1])**2
    def validSquare(self, p1, p2, p3, p4) -> bool:
        D = [self.distanceMeasure(p1,p2),
             self.distanceMeasure(p1,p3),
             self.distanceMeasure(p1,p4),
             self.distanceMeasure(p2,p3),
             self.distanceMeasure(p2,p4),
             self.distanceMeasure(p3,p4)]
        D.sort()
        return D[0]==D[1]==D[2]==D[3]!=0 and D[4] == D[5]