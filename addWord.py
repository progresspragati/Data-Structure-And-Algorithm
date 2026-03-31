class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    
    def addWord(self, word: str)->None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.endOfWord = True
    
    def search(self, word: str)->bool:
        def dfs(i, root):
            curr = root
            for j in range(i, len(word)):
                ch = word[j]
                if ch == ".":
                    for child in curr.children.values():
                        if dfs(j+1, child):
                            return True
                    return False
                else:
                    if ch not in curr.children:
                        return False
                    curr = curr.children[ch]
            return curr.endOfWord
        return dfs(0, self.root)
                    
result = WordDictionary()
result.addWord("may")
print(result.search(".ay"))