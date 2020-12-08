class Graph:

    def __init__(self):
        self.adjList = []

    def __str__(self):
        displayStr = ""
        for i in range(len(self.adjList)):
            displayStr += '('+ str(i) + ") -> "
            for edge in self.adjList[i]:
                displayStr += f"(dest:{edge[0]} cost:{edge[1]}) "
            displayStr += '\n'
        return displayStr

    def addNode(self):
        self.adjList.append([])

    def BFS(self, start, target):
        q = []
        visited = [False] * len(self.adjList)
        q.append(start)
        visited[start] = True
        while q:
            node = q.pop(0)
            for (dest, cost) in self.adjList[node]:
                if visited[dest] == False:
                    q.append(dest)
                    visited[dest] = True
                    if dest == target:
                        return True
        return False

    def DFS(self, start):
        bag_count = 0
        for (dest, cost) in self.adjList[start]:
            bag_count = bag_count + cost + cost * self.DFS(dest)        
        return bag_count

    def addEdge(self, start, end, cost):
        edge = (end, cost)
        self.adjList[start].append(edge)

input_file = open("input.txt",'r')
lines = input_file.readlines()
g = Graph()
bags = []
d = {}
bag_count = 0

for line in lines:
    bag_color = line.split("contain")[0]
    bag_color = bag_color.split(" bags")[0]
    d[bag_color] = len(g.adjList)
    bags.append(bag_color)
    g.addNode()

for i in range(len(lines)):
    line = lines[i]
    edgesStr = line.split("contain ")[1]
    edgesStr = edgesStr.split(", ")
    if i == len(lines) - 1:
        edgesStr[-1] = edgesStr[-1][:-1]
    else:
        edgesStr[-1] = edgesStr[-1][:-2]
    if edgesStr[0] == "no other bags":
        continue
    for k in range(len(edgesStr)):
        edgeStr = edgesStr[k].split(" bag")[0]
        edgeStr = edgeStr.split(' ')
        cost = int(edgeStr[0])
        destStr = ""
        for j in range(1, len(edgeStr)):
            destStr += edgeStr[j]
            if j < len(edgeStr) - 1:
                destStr += " "
        dest = d[destStr]
        g.addEdge(i, dest, cost)

for i in range(len(bags)):
    bag = bags[i]
    if bag == "shiny gold":
        continue
    target = d["shiny gold"]
    if g.BFS(i, target):
        bag_count += 1

print(f"Part one: {bag_count}")
bag_count = g.DFS(d["shiny gold"])
print(f"Part two: {bag_count}")