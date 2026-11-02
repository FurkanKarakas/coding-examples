"""
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

* PrefixTree() Initializes the prefix tree object.
* void insert(String word) Inserts the string word into the prefix tree.
* boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
* boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.
"""


class TrieNode:
    def __init__(self) -> None:
        self.charToTrieNode: dict[str, TrieNode] = dict()
        self.isTerminal: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        self.insertHelper(self.root, word, 0)

    def insertHelper(self, node: TrieNode, word: str, index: int) -> None:
        if index == len(word):
            node.isTerminal = True
            return

        currentChar = word[index]

        if currentChar not in node.charToTrieNode:
            node.charToTrieNode[currentChar] = TrieNode()
        nextTrieNode = node.charToTrieNode[currentChar]
        self.insertHelper(nextTrieNode, word, index+1)

    def search(self, word: str) -> bool:
        return self.searchHelper(self.root, word, 0)

    def searchHelper(self, node: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            return node.isTerminal
        currentChar = word[index]
        if currentChar not in node.charToTrieNode:
            return False

        nextTrieNode = node.charToTrieNode[currentChar]
        return self.searchHelper(nextTrieNode, word, index+1)

    def startsWith(self, prefix: str) -> bool:
        return self.startsWithHelper(self.root, prefix, 0)

    def startsWithHelper(self, node: TrieNode, prefix: str, index: int) -> bool:
        if index == len(prefix):
            return True

        currentChar = prefix[index]
        if currentChar not in node.charToTrieNode:
            return False

        nextTrieNode = node.charToTrieNode[currentChar]
        return self.startsWithHelper(nextTrieNode, prefix, index+1)


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))   # return True
    print(trie.search("app"))     # return False
    print(trie.startsWith("app"))  # return True
    trie.insert("app")
    print(trie.search("app"))     # return True
