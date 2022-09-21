class Trie(object):

    def __init__(self):
        self.trie = {}

    def insert(self, word):
        trie = self.trie
        for c in word:
            trie = trie.setdefault(c, {})
        trie['word'] = word
        s=2
    def search(self,word):
        trie=self.trie
        for c in word:
            if c not in trie:
                return False
            trie=trie[c]
        if 'word' in trie:
            return True
        else:
            return False

trieObj=Trie()
trieObj.insert(word="apple")
trieObj.insert(word="app")
print(trieObj.search(word="apple"))