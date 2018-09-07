
"""
Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
"""
import collections
# BFS
def findOrder1(self, numCourses, prerequisites):
    # c:pres
    dic = {i: set() for i in range(numCourses)}
    # c:posts
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    # queue stores the courses which have no prerequisites
    queue = collections.deque([i for i in dic if not dic[i]])
    count, res = 0, []
    while queue:
        node = queue.popleft()
        res.append(node)
        count += 1
        # 遍历后继课程
        for i in neigh[node]:
            dic[i].remove(node)
            if not dic[i]:
                queue.append(i)
    return res if count == numCourses else []

def test(numCourses, prerequisites):
    dic = {i: set() for i in range(numCourses)}
    neigh = collections.defaultdict(set)
    for i, j in prerequisites:
        dic[i].add(j)
        neigh[j].add(i)
    print(dic)
    print(neigh)
    queue = collections.deque([i for i in dic if not dic[i]])
    print(queue)

test(4, [[1,0],[2,0],[3,1],[3,2]])


