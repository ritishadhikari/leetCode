class Trie:

    def __init__(self):
        self.trie={}

    def insert(self, word: str) -> None:
        trie=self.trie
        for w in word:
            trie=trie.setdefault(w,{})
        trie["word"]=word

    def search(self, word: str) -> bool:
        trie=self.trie
        for w in word:
            if w not in trie: return False
            else: trie=trie[w]
        return True if 'word' in trie else False
        
    def startsWith(self, prefix: str) -> bool:
        trie=self.trie
        for w in prefix:
            if w not in trie: return False
            else: trie=trie[w]
        return True

if __name__=="__main__":
    objTrie=Trie()
    objTrie.insert(word="apple")
    objTrie.insert(word="app")
    objTrie.insert(word="monster")
    print(objTrie.search(word="app"))
    print(objTrie.search(word="mon"))
    print(objTrie.startsWith(prefix="mon"))