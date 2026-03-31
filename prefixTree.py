class TrieNode:
    def __init__(self):
        self.children = [None] * 26
        self.isEndOfWord = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()       

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if curr.children[idx] == None:
                curr.children[idx] = TrieNode()
            curr = curr.children[idx]
        curr.isEndOfWord = True

    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            idx = ord(ch) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return curr.isEndOfWord
        
    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            idx = ord(ch) - ord("a")
            if curr.children[idx] == None:
                return False
            curr = curr.children[idx]
        return True
class TrieNode1:
    def __init__(self):
        self.children = {}
        self.endOfWord = False

class PrefixTree1:
    def __init__(self):
        self.root = TrieNode1()

    def insert(self, word: str) -> None:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode1()
            curr = curr.children[ch]
        curr.endOfWord = True
    
    def search(self, word: str) -> bool:
        curr = self.root
        for ch in word:
            if ch not in curr.children:
                return False
            curr = curr.children[ch]
        return curr.endOfWord

    def startsWith(self, prefix: str) -> bool:
        curr = self.root
        for ch in prefix:
            if ch not in  curr.children:
                return False
            curr = curr.children[ch]
        return True

result = PrefixTree1()
result.insert('people')
print(result.search('people'))
print(result.startsWith('peol'))