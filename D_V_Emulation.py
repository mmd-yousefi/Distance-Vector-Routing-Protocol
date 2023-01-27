import re
import math

def bellmanford(nodes,edges,source):
    path_lengths = [ math.inf for v in nodes]
    path_lengths[source] = 0
    print(f"\nNode {source}: \n")
    count = 0
    for i in range(len(nodes) - 1):
        M = 'false'
        for (u, d), W in edges.items():
            if (path_lengths[u] != (math.inf)) and (path_lengths[u] + W < path_lengths[d]):
                print(f"Time step{count}: {path_lengths}")
                path_lengths[d] = path_lengths[u] + W
                count += 1
                M = 'true'
        if M == 'false':
            break
    print(f"Time step {count}: {path_lengths}")
    return path_lengths

#step1: Initializing
lines = []
counter = 0
node = []
edge = {}
graph = {}
neighbor = {}

#Step2: Read cost from input.txt
with open('input.txt', "r") as file:
    for line in file.readlines():
        each_line = line.strip()
        lines.append(each_line)
        counter += 1

#Step3: Create graph
for i in range(0,counter):
        line = lines[i]
        pattern  = '\d+'
        a =re.findall(pattern,line)
        vectors_int = [int(i) for i in a]
        graph[i] = vectors_int
file.close()

#Step4: Extract nodes and edges and neighbors   
for i in graph:
    node.append(i)
    for j in range(0,counter):
        temp = graph[i][j]
        if temp != 0 and temp != math.inf :
            edge[(i,j)] = temp


for i in graph:
    neigh = []
    for j in range(0,counter):
        temp = graph[i][j]
        if temp != math.inf and temp != 0 :
            neigh.append(j)
        neighbor[i] = neigh
while True:
    print("\nCommands:")
    print("update, exit")
    inp = input("Command: ")
    if inp == 'update':
        inp1 = input("Enter Source: ")
        inp2 = input("Enter Destination: ")
        if (int(inp1),int(inp2)) in edge  :
            inp3 = input("new weight: ")
            graph[int(inp1)][int(inp2)] = int(inp3)
            graph[int(inp2)][int(inp1)] = int(inp3)

            for i in graph:
                for j in range(0,counter):
                    if i != j:
                        if (j in neighbor[i]):
                            pass
                        else:
                            graph[i][j] = math.inf

            for i in graph:
                for j in range(0,counter):
                    temp = graph[i][j]
                    if temp != 0 and temp != math.inf :
                        edge[(i,j)] = temp
            for i in graph:
                    source = i
                    graph[i] = bellmanford(node,edge, source)      
        else:
            print("This Edge does not Exist")
            continue
    elif inp == 'exit':
        break
    else:
        print("Command is wrong")
