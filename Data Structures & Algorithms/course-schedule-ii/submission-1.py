class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # set graph and in_degree
        graph = defaultdict(list)
        in_degree = [0]*numCourses

        for now, pre in prerequisites:
            graph[pre].append(now)
            in_degree[now] += 1
        # set queue and visited
        q = deque([i for i in range(len(in_degree)) if in_degree[i] == 0])
        
        ans = []
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                ans.append(node)
                for neighbor in graph[node]:
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        q.append(neighbor)
        return ans if len(ans) == numCourses else []