class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.isEnd = True

    def search(self, word: str) -> bool:
        def dFS(index, node):
            if index == len(word):
                return node.isEnd
            ch = word[index]
            if ch == '.':
                for child in node.children.values():
                    if dFS(index+1, child):
                        return True
                return False
            else:
                if ch not in node.children:
                    return False
                return dFS(index + 1, node.children[ch])
        return dFS(0, self.root)
        return True

result = WordDictionary()
result.addWord("day")
result.addWord("bay")
result.addWord("may")
print(result.search("say"))
print(result.search("day"))
print(result.search(".ay"))
print(result.search("b.."))