class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # step1: Build graph and in_degree:
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for u, v in prerequisites:
            graph[v].append(u)
            in_degree[u] += 1
        # step2: Set queue and visited
        q = deque([i for i in range(len(in_degree)) if in_degree[i] == 0])
        
        # step3: BFS
        count = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                count += 1
                for n in graph[node]:
                    in_degree[n] -= 1
                    if in_degree[n] == 0:
                        q.append(n)
        return count == numCourses
                

        
