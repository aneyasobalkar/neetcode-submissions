class TrieNode:
    def __init__(self,char = None) -> None:
        self.char = char
        self.children = {}
        self.endOfWord = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()
    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            if char not in curr.children:
                curr.children[char] = TrieNode(char)
            curr = curr.children[char]
        curr.endOfWord = True
    def search(self, word: str) -> bool:
        def searchHelper(word, curr):
            if word == "" and curr.endOfWord:
                return True
            if word == "":
                return False
            char = word[0]
            if char in curr.children:
                return searchHelper(word[1:], curr.children[char])
            elif char == ".":
                for val in curr.children:
                    if searchHelper(word[1:], curr.children[val]):
                        return True
                return False
            else:
                return False  
                
        return searchHelper(word, self.root)


