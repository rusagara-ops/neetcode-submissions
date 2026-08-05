class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        adjacencylist = defaultdict(list)

        for fro, to in tickets:
            adjacencylist[fro].append(to)

        for key,value in adjacencylist.items():
            value.sort()

        result = ["JFK"]

        def dfs(node):
            if len(result) == len(tickets) + 1:
                return True

            if node not in adjacencylist:
                return False

            temp = list(adjacencylist[node])

            for index,value in enumerate(temp): #create a temporary list up here so we use it to iterate
                adjacencylist[node].pop(index)  #we can pop from original now since we are not iterating it
                result.append(value)

                if dfs(value):
                    return True
                else:
                    adjacencylist[node].insert(index,value)
                    result.pop()

            return False

        

        dfs("JFK")

        return result




