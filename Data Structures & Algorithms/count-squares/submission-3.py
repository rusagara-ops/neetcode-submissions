class CountSquares:

    def __init__(self):
        self.hashmap = {}
     

    def add(self, point: List[int]) -> None:
        tuplepoint = tuple(point)
        if tuplepoint in self.hashmap:
            self.hashmap[tuplepoint] += 1
        else:
            self.hashmap[tuplepoint] = 1


    def count(self, point: List[int]) -> int:
        ways = 0
        n = len(self.hashmap)
        for key,value in self.hashmap.items():
            diagx = key[0]
            diagy = key[1]
            qx = point[0]
            qy = point[1]
            newx = abs(diagx-qx)
            newy = abs(diagy-qy)

            if (qx,diagy) in self.hashmap and (diagx,qy) in self.hashmap:
                if newx == newy and newx != 0:
                    ways += (self.hashmap[(qx,diagy)] * self.hashmap[diagx,qy] * value)
                

        return ways
                
    
