from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    def addWord(self, word):
        cur = self
        for ch in word:
            if ch not in cur.children:
                cur.children[ch] = TrieNode()
            cur = cur.children[ch]
        cur.isWord = True
            
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode()
        for word in words:
            root.addWord(word)

        res = set()
        visit = set()
        rows = len(board)
        cols = len(board[0])
        def dFS(r, c, node, word):
            if (r < 0 or c < 0 or r == rows or c == cols or (r,c) in visit or board[r][c] not in node.children):
                return False
            visit.add((r,c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dFS(r+1, c, node, word)
            dFS(r-1, c, node, word)
            dFS(r, c+1, node, word)
            dFS(r, c-1, node, word)
            visit.remove((r,c))

        for r in range(rows):
            for c in range(cols):
                dFS(r,c,root, "")
        return list(res)

result = Solution()
print(result.findWords([["a","b","c","d"],["s","a","a","t"],["a","c","k","e"],["a","c","d","n"]], ["cat","back","backend"])) 