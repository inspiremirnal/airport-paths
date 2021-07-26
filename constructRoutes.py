import collections
from collections import defaultdict, deque
class Airports:
    def findRoutes(self, tickets: list) -> list:
        adj_list_reverse = {}
        adj_list = defaultdict(deque)
        routes = deque([])
        for f, t in tickets:
            adj_list_reverse[t] =f
            adj_list[f].append(t)
        starting_pt = [tickets[0][0]]
        for i in adj_list_reverse:
            if adj_list_reverse[i] not in adj_list_reverse:
                starting_pt = [adj_list_reverse[i]]
                break;
        while starting_pt:
            while adj_list[starting_pt[-1]]:
                starting_pt.append(adj_list[starting_pt[-1]].popleft())
            routes.appendleft(starting_pt.pop())
        return routes   
    
    def printRoutes(self, tickets: list) -> str:
        routes = self.findRoutes(tickets)
        s = "->".join(routes)
        print(s)
    
        


if __name__ == "__main__":
    a = Airports()
    a.printRoutes([["SFO","JFK"],["JFK","LHR"],["PER","SYD"],["SYD","SFO"]])
