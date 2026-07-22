class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        # create the adjacency list

        if endWord not in wordList:
            return 0

        neighbours = defaultdict(list)
        wordList.append(beginWord)

        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                neighbours[pattern].append(word)

        # now do the bfs
        visited = set(beginWord)
        queue = deque([beginWord])
        result = 1

        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result

                for i in range(len(word)):
                    pattern = word[:i] + "*" + word[i+1:]
                    for neighbour in neighbours[pattern]:
                        if neighbour not in visited:
                            queue.append(neighbour)
                            visited.add(neighbour)

            result += 1

        return 0

