class Solution:
    def one_diff(self, a, b):
        count = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                count += 1
        return count == 1

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        q = deque()
        q.append(beginWord)
        visited = set()
        visited.add(beginWord)

        step = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return step
                for word in wordList:
                    if word not in visited and self.one_diff(node, word):
                        visited.add(word)
                        q.append(word)
            step +=1
        
        return 0
