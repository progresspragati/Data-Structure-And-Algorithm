from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        res = []
        def backtrack(r,c,i):
            if i == len(word):
                return True
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
                return False
            board[r][c] = "#"
            ret = (backtrack(r+1, c, i+1) or
                   backtrack(r-1, c, i+1) or
                   backtrack(r, c+1, i+1) or
                   backtrack(r, c-1, i+1))
            board[r][c] = word[i]
            return ret
        for word in words:
            flag = False
            for r in range(rows):
                for c in range(cols):
                    if board[r][c] != word[0]:
                        continue
                    if backtrack(r,c,0):
                        res.append(word)
                        flag = True
                if flag:
                    break
        return res

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False
    
    def addWord(self, word):
        curr = self
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
        curr.isWord = True

class Solution1:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows = len(board)
        cols = len(board[0])
        res = set()
        visit = set()
        root = TrieNode()
        for word in words:
            root.addWord(word)
        
        def dfs(r, c, node, word):
            if (r < 0 or c < 0 or r >= rows or c >= cols or (r,c) in visit or board[r][c] not in node.children):
                return
            visit.add((r, c))
            node = node.children[board[r][c]]
            word += board[r][c]
            if node.isWord:
                res.add(word)
            dfs(r+1, c, node, word)
            dfs(r-1, c, node, word)
            dfs(r, c+1, node, word)
            dfs(r, c-1, node, word)
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root, "")
        
        return list(res)

class TrieNode2:
    def __init__(self):
        self.children = [None]*26
        self.idx = -1
        self.rfs = 0

    def addWord(self, word, i):
        curr = self
        for ch in word:
            if ch not in curr.children[ch]:
                curr.children[ch] = TrieNode2()
            curr = curr.children[ch] 
            curr.rfs += 1
        curr.idx = i
        
class Solution2:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        root = TrieNode2()
        for i in range(len(words)):
            root.addWord(words[i], i)
        
        rows = len(board)
        cols = len(board[0])
        res = []
        def getIndex(c):
            index = ord(c) - ord("a")
            return index

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] == "#" or not node.children[getIndex(board[r][c])]:
                return 
            temp = board[r][c]
            board[r][c] = "#"
            prev = node
            node = node.children[getIndex(temp)]
            if node.idx != -1:
                res.append(words[node.idx])
                node.idx = -1
                node.rfs = -1
                if not node.rfs:
                    prev.children[getIndex(temp)] = None
                    node = None
                    board[r][c] = temp
                    return
            dfs(r+1, c, node)
            dfs(r-1, c, node)
            dfs(r, c+1, node)
            dfs(r, c-1, node)
            board[r][c] = temp
        
        for r in range(rows):
            for c in range(cols):
                dfs(r, c, root)

        return res

    
result = Solution()
board = [
  ["a","b","c","d"],
  ["s","a","a","t"],
  ["a","c","k","e"],
  ["a","c","d","n"]
]
words = ["bat","cat","back","backend","stack"]
print(result.findWords(board, words))
result1 = Solution1()
print(result.findWords(board, words))
result2 = Solution2()
print(result.findWords(board, words))


