import time
import random
import array
import math




def SimulatedAnneling(G):
    s = list(range(len(G)))
    c = cost(G, s)
    ntrial = 1
    T = 30
    alpha = 0.99
    for i in range(1000000):
        n = random.randint(0, len(G) - 1)
        while True:
            m = random.randint(0, len(G) - 1)
            if n != m:
                break
        s1 = swap(s, m, n)
        c1 = cost(G, s1)
        if c1 < c:
            s, c = s1, c1
        else:
            if random.random() < pow(math.e, -(c1 - c) / T):
                s, c = s1, c1
        T = alpha * T
    return s

def swap(s, m, n):
    i, j = min(m, n), max(m, n)
    s1 = s[:]
    while i < j:
        s1[i], s1[j] = s1[j], s1[i]
        i += 1
        j -= 1
    return s1
  
def cost(G, s):
    l = 0
    for i in range(len(s)-1):
        l += G[s[i]][s[i+1]]
    l += G[s[len(s)-1]][s[0]] 
    return l



def calc_cost(dist_matrix, path):
    cost = 0
    n = len(dist_matrix)
    i = 0
    while i < n - 1:
        start_node = path[i]
        end_node = path[i + 1]
        cost += dist_matrix[end_node][start_node]
        i += 1

    cost += dist_matrix[path[-1]][path[0]]

    return cost


def BNB(G):
    start_time = time.time()
    n = len(G)
    final_nodes = [i for i in range(1, n)]
    final_path = None
    final_cost = float('inf')
    stack = [(0, [0], 0)]
    
    i = 0
    while stack and i < 1000000:  # Limited iterations for performance
        current_node, path, cost = stack.pop()
        
        if len(path) == n:  # All nodes visited
            cost += G[path[-1]][0]  # Return to the starting node
            if cost < final_cost:
                final_cost = cost
                final_path = path
            continue
        
        for node in final_nodes:
            if node not in path:
                new_cost = cost + G[current_node][node]
                if new_cost < final_cost:
                    new_path = path + [node]
                    stack.append((node, new_path, new_cost))
        
        i += 1
        if time.time() - start_time > 280:
            return final_path
    
    return final_path





# Input
g = input().strip()
n = int(input().strip())

v = []
for _ in range(n):
    v.append(tuple(map(float, input().strip().split())))

d = []
for _ in range(n):
    d.append(list(map(float, input().strip().split())))

ini_sa = SimulatedAnneling(d)
print(*ini_sa)
if n <= 10:
    opt = BNB(d)
    print(opt)

    

    if calc_cost(d, opt) < calc_cost(d, ini_sa):
        print(*opt)
    else:
        print(*ini_sa)
