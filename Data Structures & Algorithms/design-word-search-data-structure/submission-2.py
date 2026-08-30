class TrieNode:
    def __init__(self):
        self.children = {}
        self.endofword = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        curr = self.root

        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]

        curr.endofword = True
        

    def search(self, word: str) -> bool:
        def dfs(j, root):
            curr = root
            for i in range(j,len(word)):
                char = word[i]
                if char == ".": #we use backttracking/ recursion to go down the 26 characters
                    for child in curr.children.values():
                        if dfs(i+1, child):
                            return True
                        return False
                else:
                    if char not in curr.children:
                        return False
                    curr = curr.children[char]
            return curr.endofword
        return dfs(0,self.root)
        
