class WordDictionary:

    def __init__(self):
        self.container={}

    def addword(self, word:str) ->None:
        wordLength=len(word)
        if wordLength not in self.container:
            self.container[wordLength]=set()
            self.container[wordLength].add(word)
        else:
            self.container[wordLength].add(word)

    def search(self,word:str) -> bool:
        wordLength=len(word)
        if wordLength not in self.container:
            return False
        elif "." not in word:
            return True if word in self.container[wordLength] else False
        else:
            possibleWords=self.container[wordLength]
            for pw in possibleWords:
                success=True
                for ind,ch in enumerate(word):
                    if pw[ind]!=ch and ch!=".":
                        success=False
                        break
                if success:
                    return True
            return False
                        


if __name__=="__main__":
    obj=WordDictionary()
    obj.addword(word="bad")
    obj.addword(word="dad")
    obj.addword(word="mad")
    obj.search(word="pad")
    obj.search(word="bad")
    obj.search(word=".ad")
    obj.search(word="b..")

