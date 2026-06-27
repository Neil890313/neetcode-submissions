class Solution:
    def oneDiff(self, a, b):
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

        count = 1
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node == endWord:
                    return count
                for word in wordList:
                    if self.oneDiff(node, word) and word not in visited:
                        visited.add(word)
                        q.append(word)
            count += 1
        return 0
